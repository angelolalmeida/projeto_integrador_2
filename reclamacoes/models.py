from django.db import models
from django.utils import timezone

# Create your models here.
STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('verificado', 'Verificado'),
        ('resolvido', 'Resolvido'),
        ('nao_resolvido', 'Não Resolvido'),
    ]

TIPO_RECLAMACAO_CHOICES = [
    ('nao_recebi', 'Não recebi o saco verde'),
    ('caminhao_nao_passou', 'Caminhão não passou'),
    ('saco_rasgado', 'Saco rasgado'),
    ('outros', 'Outros'),
]

BAIRROS_CHOICES = [
    ('area_rural_macatuba', 'Área Rural de Macatuba'),
    ('centro', 'Centro'),
    ('distrito_industrial_mario_alves_nunes', 'Distrito Industrial Mario Alves Nunes'),
    ('jardim_bem_viver', 'Jardim Bem Viver'),
    ('jardim_capri', 'Jardim Capri'),
    ('jardim_esperanca', 'Jardim Esperança'),
    ('jardim_panorama', 'Jardim Panorama'),
    ('jardim_planalto', 'Jardim Planalto'),
    ('jardim_santa_ana', 'Jardim Santa Ana'),
    ('jardim_santa_clara', 'Jardim Santa Clara'),
    ('jardim_santo_antonio', 'Jardim Santo Antonio'),
    ('jardim_sonho_meu', 'Jardim Sonho Meu'),
    ('jardim_veneza', 'Jardim Veneza'),
    ('nucleo_habitacional_antonio_lorenzetti', 'Núcleo Habitacional Antônio Lorenzetti'),
    ('nucleo_habitacional_jardim_america', 'Núcleo Habitacional Jardim América'),
    ('nucleo_habitacional_jardim_bocayuva', 'Núcleo Habitacional Jardim Bocayuva'),
    ('nucleo_habitacional_jardim_europa', 'Núcleo Habitacional Jardim Europa'),
    ('nucleo_habitacional_joao_leme_do_prado', 'Núcleo Habitacional João Leme do Prado'),
    ('nucleo_habitacional_vila_nova', 'Núcleo Habitacional Vila Nova'),
    ('residencial_azevedo', 'Residencial Azevedo'),
    ('residencial_riviera', 'Residencial Riviera'),
    ('vale_verde', 'Vale Verde'),
    ('vila_do_saber', 'Vila do Saber'),
]

class Reclamacoes(models.Model):
    tipo_reclamacao = models.CharField(max_length=20, choices=TIPO_RECLAMACAO_CHOICES, default='outros',)
    observacao = models.TextField(max_length=500)
    rua = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=100, choices=BAIRROS_CHOICES)
    numero_casa = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', editable=False)
    historico = models.TextField(blank=True, null=True, editable=False)
    data_criacao = models.DateTimeField(default=timezone.now, editable=False)

    # Outros campos do modelo Reclamacao

    def __str__(self):
        return f"Reclamação {self.id}"

    class Meta:
        db_table = 'reclamacoes'
        verbose_name_plural = 'Reclamações'
        verbose_name = 'Reclamação'
        # ordering = ['nome']