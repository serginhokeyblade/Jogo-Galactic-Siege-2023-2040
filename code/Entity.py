#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        # Inicializa a entidade com nome e posição
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]  # Atribui a saúde conforme a entidade
        self.damage = ENTITY_DAMAGE[self.name]  # Atribui o dano conforme a entidade
        self.score = ENTITY_SCORE[self.name]  # Atribui a pontuação conforme a entidade
        self.last_dmg = 'None'  # Inicializa o último dano como 'None'

    @abstractmethod
    def move(self):
        # Método abstrato que deve ser implementado nas subclasses para movimentação
        pass
