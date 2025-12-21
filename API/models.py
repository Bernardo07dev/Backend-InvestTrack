from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Investimentos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.CharField(max_length=100)
    ticker = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    data = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    img = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.stock
class Carteira(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    investido = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Transacao(models.Model):
    escolhas = (
        ('adicionar', 'adicionar'),
        ('subtrair', 'subtrair')
    )
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    transaction = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=escolhas)