#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        # Inicializa o inimigo com nome e posição, e define o atraso do tiro
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        # Move o inimigo para a esquerda de acordo com sua velocidade
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        # Diminui o atraso do tiro e dispara o tiro do inimigo quando o atraso chega a zero
        self.shot_delay -= 1
        if self.shot_delay == 0:
            # Reseta o atraso do tiro e retorna um novo tiro do inimigo
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
