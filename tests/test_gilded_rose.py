import pytest
from gilded_rose import GildedRose, Item


@pytest.mark.parametrize(
    "name, sell_in, quality, expected_sell_in, expected_quality",
    [
        # Itens Comuns
        ("item comum", 10, 20, 9, 19),
        ("item comum", 0, 20, -1, 18),  # Vencido degrada o dobro
        ("item comum", 5, 0, 4, 0),    # Qualidade nunca menor que 0
        
        # Envelhece melhorando
        ("Aged Brie", 2, 0, 1, 1),
        ("Aged Brie", 2, 50, 1, 50),   # Qualidade não passa de 50
        
        # Lendário, nada muda
        ("Sulfuras, Hand of Ragnaros", 0, 80, 0, 80),
        
        # Ingressos para o show
        ("Backstage passes to a TAFKAL80ETC concert", 15, 20, 14, 21), # > 10 dias +1
        ("Backstage passes to a TAFKAL80ETC concert", 10, 20, 9, 22),  # <= 10 dias +2
        ("Backstage passes to a TAFKAL80ETC concert", 5, 20, 4, 23),   # <= 5 dias +3
        ("Backstage passes to a TAFKAL80ETC concert", 0, 20, -1, 0),    # Após o show - vira 0
    
        # Itens Conjured - Degradam o dobro: 2 normais, 4 vencidos
        ("Conjured Mana Cake", 3, 6, 2, 4),
        ("Conjured Mana Cake", 0, 6, -1, 2),
    
    ],
)
def test_gilded_rose_update(name, sell_in, quality, expected_sell_in, expected_quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    
    assert items[0].sell_in == expected_sell_in
    assert items[0].quality == expected_quality