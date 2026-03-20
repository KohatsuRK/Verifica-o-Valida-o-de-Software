import unittest
class RaceRegistration:
    @staticmethod
    def verificar_cadastro(participante):
        idade = participante.get('idade')
        categoria = participante.get('categoria')
        tempo = participante.get('tempo')
        assinado = participante.get('termo_assinado')

        # Regra 1: Idade
        if not (10 <= idade <= 60):
            return "Erro: Idade fora da faixa permitida (10-60)."

        # Regra 2: Categoria (Consistência com a idade)
        if 10 <= idade <= 14 and categoria != 'infantil':
            return "Erro: Categoria deve ser 'infantil'."
        elif 15 <= idade <= 17 and categoria != 'juvenil':
            return "Erro: Categoria deve ser 'juvenil'."
        elif 18 <= idade <= 60 and categoria != 'adulto':
            return "Erro: Categoria deve ser 'adulto'."

        # Regra 3: Tempo
        if not (30 <= tempo <= 180):
            return "Erro: Tempo estimado deve ser entre 30 e 180 min."

        # Regra 4: Assinatura
        if not assinado:
            return "Erro: Termo de responsabilidade deve ser assinado."

        return "Cadastro Válido"
    



class TestRaceRegistration(unittest.TestCase):
    
    # Teste de Sucesso (Caminho Feliz)
    def test_cadastro_valido(self):
        p = {'idade': 25, 'categoria': 'adulto', 'tempo': 45, 'termo_assinado': True}
        self.assertEqual(RaceRegistration.verificar_cadastro(p), "Cadastro Válido")

    # Testes de Idade (Rule 1)
    def test_idade_abaixo_limite(self):
        p = {'idade': 9, 'categoria': 'infantil', 'tempo': 60, 'termo_assinado': True}
        self.assertIn("Idade fora da faixa", RaceRegistration.verificar_cadastro(p))

    # Testes de Categoria (Rule 2)
    def test_categoria_incompativel(self):
        p = {'idade': 12, 'categoria': 'adulto', 'tempo': 60, 'termo_assinado': True}
        self.assertIn("Categoria deve ser 'infantil'", RaceRegistration.verificar_cadastro(p))

    # Testes de Tempo (Rule 3)
    def test_tempo_excedido(self):
        p = {'idade': 30, 'categoria': 'adulto', 'tempo': 200, 'termo_assinado': True}
        self.assertIn("Tempo estimado deve ser entre 30 e 180", RaceRegistration.verificar_cadastro(p))

    # Testes de Assinatura (Rule 4)
    def test_sem_assinatura(self):
        p = {'idade': 30, 'categoria': 'adulto', 'tempo': 60, 'termo_assinado': False}
        self.assertIn("Termo de responsabilidade deve ser assinado", RaceRegistration.verificar_cadastro(p))

if __name__ == '__main__':
    unittest.main()