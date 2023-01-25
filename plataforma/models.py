from django.db import models
from django.contrib.auth.models import User

class Pacientes(models.Model):
    choices_sexo = (('F', 'Feminino'),
                    ('M', 'Maculino'))
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    nutri = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class DadosPaciente(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data = models.DateTimeField()
    peso = models.FloatField()
    altura = models.FloatField()
    biceps = models.FloatField()
    triceps = models.FloatField()
    axilar_media = models.FloatField()
    torax = models.FloatField()
    abdominal = models.FloatField()
    suprailiaca = models.FloatField()
    subescapular = models.FloatField()
    coxa = models.FloatField()
    panturrilha = models.FloatField()
    peitoral = models.FloatField()
    abdomen = models.FloatField()
    cintura = models.FloatField()
    quadril = models.FloatField()
    pescoco = models.FloatField()
    coxa_e = models.FloatField()
    coxa_d = models.FloatField()
    panturrilha_e = models.FloatField()
    panturrilha_d = models.FloatField()
    punho_e = models.FloatField()
    punho_d = models.FloatField()
    braco_e = models.FloatField()
    braco_d = models.FloatField()
    antebraco_e = models.FloatField()
    antebraco_d = models.FloatField()

    def __str__(self):
        return f"Paciente({self.paciente.nome}, {self.peso})"

    


