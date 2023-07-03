from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields = ('id', 'owner', 'name', 'recipe_box', 'created_at', 'updated_at')