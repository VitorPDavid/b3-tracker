from django.db import models
from django.conf import settings


class Asset(models.Model):
    code = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=50)
    max_price = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    min_price = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    last_price = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    last_price_date = models.DateTimeField(null=True)


class AssetPrice(models.Model):
    asset = models.ForeignKey(
        Asset,
        related_name="price_history",
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=12, decimal_places=3)

    class Meta:
        unique_together = [["asset", "date"]]

    def save(self, *args, **kwargs):
        self.fix_asset_values()
        return super().save(*args, **kwargs)

    def fix_asset_values(self):
        """
        Garantindo que os valores do ativo estajam corretos com o novo valor buscado
        mantido nesse model para consistencia de dados
        """
        if not self.asset.max_price or self.price > self.asset.max_price:
            self.asset.max_price = self.price

        if not self.asset.min_price or self.price < self.asset.min_price:
            self.asset.min_price = self.price

        self.asset.last_price = self.price
        self.asset.last_price_date = self.date

        self.asset.save()


class TradingTunnel(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
    )
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
    )

    bottom_value = models.DecimalField(max_digits=12, decimal_places=3)
    top_value = models.DecimalField(max_digits=12, decimal_places=3)
