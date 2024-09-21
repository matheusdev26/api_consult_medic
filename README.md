# API de Profissionais e Consultas

## Esta é uma API desenvolvida com Flask para gerenciar profissionais e consultas.

Requisitos:
 
- Python 3.x
- flask

Crie um ambiente virtual:
- python -m venv venv

Instale as dependências:
pip install Flask

Para rodar a aplicação, utilize o comando:
python app.py

Adicionar um Profissional:

    curl -X POST http://127.0.0.1:5000/profissionais -H "Content-Type: application/json" -d '{"full_name": "Dr. Marcos Antônio", "social_name": "Marcos", "profession": "Médico", "address": "123 Rua Mônica", "contact": "1234567890"}'
     
Adicionar uma consulta:

    curl -X POST http://127.0.0.1:5000/consultas -H "Content-Type: application/json" -d '{"date": "2024-09-20", "profissional_id": 1}'
    
Pesquisar Consultas:

    curl http://127.0.0.1:5000/consultas/profissionais/1

