import unittest
import product


class TestProduct(unittest.TestCase):

    def test_prod_init(self):
        shirt = product.Product("shirt", 10, 500)
        self.assertEqual(shirt.price, 500)
        watch = product.Product("wrist watch", 100, 1200)
        self.assertEqual(watch.price, 1200)
        book = product.Product("textbook", 200, 800)
        self.assertEqual(book.price, 800)
        hBook = product.Product("history book", 300, 500)
        self.assertEqual(hBook.price, 500)
        mCard = product.Product("memory card", 400, 1400)
        self.assertEqual(mCard.price, 1400)

    def test_prod_get_price(self):
        shirt = product.Product("shirt", 12, 500)
        self.assertEqual(shirt.get_price(5), 2500)
        watch = product.Product("wrist watch", 100, 1200)
        self.assertEqual(watch.get_price(3), 3600)
        book = product.Product("textbook", 200, 800)
        self.assertEqual(book.get_price(2), 1600)
        hBook = product.Product("history book", 300, 500)
        self.assertEqual(hBook.get_price(3), 1500)
        mCard = product.Product("memory card", 400, 1400)
        self.assertEqual(mCard.get_price(2), 2800)

    def test_prod_make_purchase(self):
        shirt = product.Product("shirt", 12, 500)
        self.assertEqual(shirt.make_purchase(2), 10)
        mCard = product.Product("memory card", 400, 1400)
        self.assertEqual(mCard.make_purchase(200), 200)
        book = product.Product("textbook", 200, 800)
        with self.assertRaises(ValueError):
            book.make_purchase(202)

    def test_convert_inches(self):
        c = product.Converter(9, "inches")
        self.assertEqual(c.feet(), 0.75)
        self.assertEqual(c.centimeters(), 22.86)
        self.assertEqual(c.meters(), 0.23)
        self.assertEqual(c.inches(), 9)

    def test_convert_feet(self):
        c = product.Converter(3, "feet")
        self.assertEqual(c.feet(), 3)
        self.assertEqual(c.inches(), 36)
        self.assertEqual(c.yards(), 1)

    def test_convert_miles(self):
        c = product.Converter(10, "miles")
        self.assertEqual(c.kilometers(), 16.09)
        self.assertEqual(c.inches(), 633600)

    def test_convert_centimeters(self):
        c = product.Converter(200, "centimeters")
        self.assertEqual(c.feet(), 6.56)
        self.assertEqual(c.inches(), 78.74)
        self.assertEqual(c.yards(), 2.19)


if __name__ == "__main__":
    unittest.main()
