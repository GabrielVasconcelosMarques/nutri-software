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

    def get_imc(self):
        return round(float(self.peso) / float((self.altura**2)/10000), 2)

    def imc_situacao(self):
        retorno = self.get_imc()
        if retorno < 18.5:
            return 'Abaixo do peso normal'
        elif retorno < 24.9:
            return 'Peso normal'
        elif retorno < 29.9:
            return 'Excesso de peso'
        elif retorno < 34.9:
            return 'Obesidade classe I'
        elif retorno < 39.9:
            return 'Obesidade classe II'
        elif retorno >= 40:
            return 'Obesidade classe III'

    def get_peso_ideal(self):
        altura_quadrado_em_metros = (self.altura**2 / 10000)
        if self.paciente.sexo == 'F':
            return round(altura_quadrado_em_metros * 21, 2)
        elif self.paciente.sexo == 'M':
            return round(altura_quadrado_em_metros * 22, 2)

    def get_massa_gorda_percentual(self):
        # (1,20 x 19,68) + (0,23 x 27) – (10,8 x 1) – 5.4
        imc = self.get_imc()
        idade = self.paciente.idade
        if self.paciente.sexo == 'F':
            return round((1.20 * imc) + (0.23 * idade) - (10.3 * 0) - 5.4, 2)
        elif self.paciente.sexo == 'M':
            return round((1.20 * imc) + (0.23 * idade) - (10.3 * 1) - 5.4, 2)

    def get_massa_gorda_situacao_percentual(self):
        massa_gorda = self.get_massa_gorda_percentual()
        if massa_gorda <= 20:
            return 'Bom'
        else:
            return 'Ruim'

    def get_massa_magra_percentual(self):
        return round((self.get_massa_gorda_percentual() - 100) * -1, 2)


    def get_massa_magra_situacao_percentual(self):
        massa_magra = self.get_massa_magra_percentual()
        if massa_magra >= 80 and massa_magra <= 92:
            return 'Bom'
        else:
            return 'Ruim'

    
    def get_massa_gorda(self):
        peso = self.peso
        massa_gorda = self.get_massa_gorda_percentual()
        calculo = peso*massa_gorda / 100
        return round(calculo, 2)

    def get_massa_gorda_inicial(self):
        peso = self.peso
        calculo = peso* 8 / 100
        return round(calculo, 2)

    def get_massa_gorda_final(self):
        peso = self.peso
        calculo = peso* 20 / 100
        return round(calculo, 2)

    def get_massa_gorda_status(self):
        massa_gorda = self.get_massa_gorda()
        massa_gorda_inicial = self.get_massa_gorda_inicial()
        massa_gorda_final = self.get_massa_gorda_final()

        if massa_gorda_inicial <= massa_gorda <= massa_gorda_final:
            return 'Bom'
        else:
            return 'Ruim'


    def get_massa_magra(self):
        peso = self.peso
        massa_magra= self.get_massa_magra_percentual()
        calculo = peso*massa_magra / 100
        return round(calculo, 2)

    def get_massa_magra_inicial(self):
        peso = self.peso
        calculo = peso* 80 / 100
        return round(calculo, 2)

    def get_massa_magra_final(self):
        peso = self.peso
        calculo = peso* 92 / 100
        return round(calculo, 2)

    def get_massa_magra_status(self):
        massa_magra = self.get_massa_magra()
        massa_magra_inicial = self.get_massa_magra_inicial()
        massa_magra_final = self.get_massa_magra_final()

        if massa_magra_inicial <= massa_magra <= massa_magra_final:
            return 'Bom'
        else:
            return 'Ruim'


    def get_soma_dobras(self):
        return round(self.biceps + self.triceps + self.axilar_media + self.torax + self.panturrilha + self.abdominal + self.subescapular + self.suprailiaca + self.coxa, 2)


    def get_razao_cintura_quadril(self):
        cintura = self.cintura
        quadril = self.quadril

        return round(cintura/quadril, 2)

    def get_razao_cintura_quadril_status(self):
        razao = self.get_razao_cintura_quadril()
        if self.paciente.sexo == 'F':
            if razao < 0.80:
                return 'Baixo'
            elif razao < 0.85:
                return 'Moderado'
            else:
                return 'Alto'

        elif self.paciente.sexo == 'M':
            if razao < 0.95:
                return 'Baixo'
            elif razao < 1.0:
                return 'Moderado'
            else:
                return 'Alto'

    def get_amb(self):
        comprimento_braco = self.braco_d
        triceps = self.triceps
        resultado = ((comprimento_braco - (0.314 * triceps))**2) / 12.56

        return round(resultado, 2)

    def get_cmb(self):
        comprimento_braco = self.braco_d
        triceps = self.triceps
        resutado = comprimento_braco - (0.314 * triceps)

        return round(resutado, 2)

    def get_agb(self):
        comprimento_braco = self.braco_d
        triceps = self.triceps

        a = (comprimento_braco * (triceps/10)) / 2
        b = (3.14 * (7/10)**2) / 4

        return round(a - b, 2)


    
            
        


