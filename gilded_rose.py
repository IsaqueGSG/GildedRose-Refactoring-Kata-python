# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            
            # Sulfuras nunca sofre alterações
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # atualiza qualidade usando tipo de item
            if item.name == "Aged Brie":
                self._atualizar_aged_brie(item)

            elif item.name.startswith("Backstage passes"):
                self._atualizar_backstage_pass(item)

            elif item.name.startswith("Conjured"):
                self._atualizar_conjured(item)

            else:
                self._atualizar_item_comum(item)

            # Reduzvalidade de todos os outros itens
            item.sell_in -= 1

            self._limitar_qualidade(item)

    def _atualizar_item_comum(self, item):
        # Itens normais perdem o dobro de qualidade se já estiverem vencidos
        taxa_degradacao = 2 if item.sell_in <= 0 else 1
        item.quality -= taxa_degradacao

    def _atualizar_aged_brie(self, item):
        # Aged Brie ganha mais qualidade se já estiver vencido
        taxa_valorizacao = 2 if item.sell_in <= 0 else 1
        item.quality += taxa_valorizacao

    def _atualizar_backstage_pass(self, item):
        # Aumenta o preço do ingresso perto do Show
        # Zera o valor depois do Shopw
        if item.sell_in <= 0:
            item.quality = 0

        elif item.sell_in <= 5:
            item.quality += 3

        elif item.sell_in <= 10:
            item.quality += 2

        else:
            item.quality += 1

    def _atualizar_conjured(self, item):
        # Itens Conjured estragam o dobro da velocidade dos normais
        taxa_degradacao = 4 if item.sell_in <= 0 else 2
        item.quality -= taxa_degradacao

    def _limitar_qualidade(self, item):
        # qualidade ente 0 e 50
        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)