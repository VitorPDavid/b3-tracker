from decimal import Decimal
import pytest
from django.utils import timezone
from trading_tunnel_alerts.models import Asset, AssetPrice


@pytest.mark.django_db
class TestAssets:
    def test_create_new_AssetPrice_changes_assets_values_correctly(self):
        test_asset = Asset.objects.create(code="TEST3", name="A test asset")

        assert test_asset.max_price is None
        assert test_asset.min_price is None
        assert test_asset.last_price is None
        assert test_asset.last_price_date is None

        mock_now = timezone.now()
        AssetPrice.objects.create(asset=test_asset, price=Decimal("34"), date=mock_now)

        assert test_asset.max_price == Decimal("34")
        assert test_asset.min_price == Decimal("34")
        assert test_asset.last_price == Decimal("34")
        assert test_asset.last_price_date == mock_now

    def test_create_AssetPrice_with_new_mim_value_changes_mim_price_correctly(self):
        test_asset = Asset.objects.create(code="TEST3", name="A test asset")

        assert test_asset.max_price is None
        assert test_asset.min_price is None
        assert test_asset.last_price is None
        assert test_asset.last_price_date is None

        mock_now = timezone.now()
        AssetPrice.objects.create(asset=test_asset, price=Decimal("34"), date=mock_now)

        assert test_asset.max_price == Decimal("34")
        assert test_asset.min_price == Decimal("34")
        assert test_asset.last_price == Decimal("34")
        assert test_asset.last_price_date == mock_now

        AssetPrice.objects.create(asset=test_asset, price=Decimal("30"), date=mock_now)

        assert test_asset.max_price == Decimal("34")
        assert test_asset.min_price == Decimal("30")
        assert test_asset.last_price == Decimal("30")
        assert test_asset.last_price_date == mock_now

    def test_create_AssetPrice_with_new_max_value_changes_max_price_correctly(self):
        test_asset = Asset.objects.create(code="TEST3", name="A test asset")

        assert test_asset.max_price is None
        assert test_asset.min_price is None
        assert test_asset.last_price is None
        assert test_asset.last_price_date is None

        mock_now = timezone.now()
        AssetPrice.objects.create(asset=test_asset, price=Decimal("34"), date=mock_now)

        assert test_asset.max_price == Decimal("34")
        assert test_asset.min_price == Decimal("34")
        assert test_asset.last_price == Decimal("34")
        assert test_asset.last_price_date == mock_now

        AssetPrice.objects.create(
            asset=test_asset, price=Decimal("35.05"), date=mock_now
        )

        assert test_asset.max_price == Decimal("35.05")
        assert test_asset.min_price == Decimal("34")
        assert test_asset.last_price == Decimal("35.05")
        assert test_asset.last_price_date == mock_now
