import unittest
from validador_cpf import validar_cpf, formatar_cpf

class TestValidadorCPF(unittest.TestCase):
    
    def test_cpf_valido_com_pontos(self):
        """Testa CPF válido com formatação (CPF 529.982.247-25 é válido)"""
        self.assertTrue(validar_cpf("529.982.247-25"))
    
    def test_cpf_valido_sem_pontos(self):
        """Testa CPF válido sem formatação"""
        self.assertTrue(validar_cpf("52998224725"))
    
    def test_cpf_invalido(self):
        """Testa CPF inválido conhecido"""
        self.assertFalse(validar_cpf("123.456.789-00"))
    
    def test_cpf_todos_digitos_iguais(self):
        """Testa CPF com todos dígitos iguais (inválido por definição)"""
        self.assertFalse(validar_cpf("111.111.111-11"))
    
    def test_cpf_tamanho_incorreto(self):
        """Testa CPF com tamanho diferente de 11 dígitos"""
        self.assertFalse(validar_cpf("12345"))
        self.assertFalse(validar_cpf("123456789012"))  # 12 dígitos
    
    def test_cpf_com_letras(self):
        """Testa CPF com caracteres não numéricos além de pontos e traços"""
        self.assertFalse(validar_cpf("529.982.ABC-25"))
    
    def test_formatacao_cpf(self):
        """Testa a função de formatação"""
        self.assertEqual(formatar_cpf("52998224725"), "529.982.247-25")
        self.assertEqual(formatar_cpf("529.982.247-25"), "529.982.247-25")

if __name__ == "__main__":
    print("Rodando testes do validador de CPF...")
    unittest.main()
