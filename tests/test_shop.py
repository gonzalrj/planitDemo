import pytest

from page_objects.cart_page import CartPage
from page_objects.shop_page import ShopPage


class TestAddingProductsToCart:
    """
    Test case 3:
    1. Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
    2. Go to the cart page
    3. Verify the subtotal for each product is correct
    4. Verify the price for each product
    5. Verify that total = sum(sub-totals)
    """
    @pytest.mark.planit
    def test_checkout(self, driver, base_url, qty_stuffed_frog=2, qty_fluffy_bunny=5, qty_valentine_bear=3):
        shop_page = ShopPage(driver)
        shop_page.goto_page_new_session(base_url + "/#/shop")

        unit_price_stuffed_frog = shop_page.get_unit_price_as_float("stuffed frog")
        shop_page.add_to_cart("stuffed frog", qty_stuffed_frog)
        line_total_stuffed_frog = unit_price_stuffed_frog * qty_stuffed_frog

        unit_price_fluffy_bunny = shop_page.get_unit_price_as_float("fluffy bunny")
        shop_page.add_to_cart("fluffy bunny", qty_fluffy_bunny)
        line_total_fluffy_bunny = unit_price_fluffy_bunny * qty_fluffy_bunny

        unit_price_valentine_bear = shop_page.get_unit_price_as_float("valentine bear")
        shop_page.add_to_cart("valentine bear", qty_valentine_bear)
        line_total_valentine_bear = unit_price_valentine_bear * qty_valentine_bear

        shop_page.goto_cart()

        # Verify that the unit price from the Shop page is still the same with the Cart page.
        cart_page = CartPage(driver)

        assert cart_page.get_unit_price("stuffed frog") == unit_price_stuffed_frog, "Discrepancy in the unit price."
        assert cart_page.get_unit_price("fluffy bunny") == unit_price_fluffy_bunny, "Discrepancy in the unit price."
        assert cart_page.get_unit_price("valentine bear") == unit_price_valentine_bear, "Discrepancy in the unit price."

        # Verify that the subtotal per product is correct.
        assert cart_page.get_unit_subtotal("stuffed frog") == line_total_stuffed_frog, \
            "Discrepancy in the line computation."
        assert cart_page.get_unit_subtotal("fluffy bunny") == line_total_fluffy_bunny, \
            "Discrepancy in the line computation."
        assert cart_page.get_unit_subtotal("valentine bear") == line_total_valentine_bear, \
            "Discrepancy in the line computation."

        # Verify that the total price is correct.
        assert (cart_page.get_total_price() ==
                (line_total_stuffed_frog + line_total_fluffy_bunny + line_total_valentine_bear)), \
            "Discrepancy in the total computation."
