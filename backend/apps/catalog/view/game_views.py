from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decimal import Decimal, InvalidOperation
from apps.catalog.dto.game_dto import CreateGameDTO
from apps.catalog.service.game_service import GameServiceCreate

@method_decorator(csrf_exempt, name="dispatch")
class GameCreateApiView(View):
    def post(self, request):
        try:
            name = request.POST.get("name")
            release_date = request.POST.get("release_date")
            genre = request.POST.get("genre")
            publisher = request.POST.get("publisher")
            price_raw = request.POST.get("price")
            if not all([name, release_date, genre, publisher, price_raw]):
                return JsonResponse({"error": "Todos os campos obrigatórios devem ser preenchidos"}, status=400)
            try:
                price = Decimal(price_raw)
            except (InvalidOperation, TypeError):
                return JsonResponse({"error": "Preço inválido"}, status=400)
            images = request.FILES.getlist("images")[:3]
            dto = CreateGameDTO(
                name=name,
                release_date=release_date,
                genre=genre,
                publisher=publisher,
                price=price,
                images=images
            )
            game = GameServiceCreate.create_game(dto)
            return JsonResponse({
                "id": game.id,
                "name": game.name,
                "game_tag": game.game_tag,
                "genre": game.genre,
                "price": str(game.price),
                "publisher": game.publisher,
                "images": [request.build_absolute_uri(img.image.url) for img in game.images.all()]
            }, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
