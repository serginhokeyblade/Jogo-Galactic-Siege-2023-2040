#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        # Dependendo do nome da entidade, cria diferentes tipos de objeto
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                # Cria o fundo para o nível 1 com várias imagens
                for i in range(3):  # número de imagens de Level1Bg
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                # Cria o fundo para o nível 2 com várias imagens
                for i in range(5):   # número de imagens de Level2Bg
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                # Cria o jogador 1 na posição inicial
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                # Cria o jogador 2 na posição inicial
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                # Cria o inimigo 1 em uma posição aleatória
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                # Cria o inimigo 2 em uma posição aleatória
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
