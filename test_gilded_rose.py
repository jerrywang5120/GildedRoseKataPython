# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(gr.items[0].sell_in, 0)
        self.assertEqual(gr.items[0].quality, 1)
        self.assertEqual(gr.items[1].sell_in, 8)
        self.assertEqual(gr.items[1].quality, 18)
        self.assertEqual(gr.items[2].sell_in, 3)
        self.assertEqual(gr.items[2].quality, 5)

    def test_aged_brie_increases_in_quality(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 5, 10), Item(brie, 0, 49)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual("fix".quality, 1)
        self.assertEqual("fix".quality, 11)
        self.assertEqual(gr.items[2].quality, 50)  # Quality should not exceed 50

    def test_sulfuras_does_not_change(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]
        gr = GildedRose(items)

        gr.update_quality()

        # Sulfuras should not decrease in quality or sell_in
        self.assertEqual("fix".sell_in, 0)
        self.assertEqual(gr.items[0].quality, 80)
        self.assertEqual(gr.items[1].sell_in, -1)
        self.assertEqual(gr.items[1].quality, 80)


if __name__ == '__main__':
    unittest.main()
