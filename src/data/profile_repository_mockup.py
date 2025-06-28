import pandas as pd

class ProfileRepositoryMockup:
    def get_profiles_data(self) -> pd.DataFrame:
        data = {
            'id': [0, 1, 2, 3, 4, 5],
            'title': [
                'Conglomerado Institucional', 
                'Tesouraria Institucional / Gestora de Ativos',
                'Cooperativa / Grande Empresa Agro (PJ Agro)',
                'Produtor Rural (Pessoa Física)',
                'Empresa Comercial Tomadora de Crédito',
                'Cliente de Varejo Padrão'
            ],
            'description': [
                'Clientes com perfil corporativo, de grande porte',
                'Instituições focadas em acumulação e gestão de liquidez',
                'Empresas rurais com atuação intensiva no agronegócio',
                'Indivíduos vinculados ao setor agrícola',
                'PMEs urbanas com alta demanda por capital de giro',
                'Pessoa física com uso mínimo de produtos financeiros'
            ],
            'color': [
                '#002776', '#FFDE00', '#2E8B57', '#4B0082', '#ADFF2F', '#FF69B4',
            ]
        }
        return pd.DataFrame(data)
