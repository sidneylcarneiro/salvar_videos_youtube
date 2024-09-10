
```markdown
# Vídeo Downloader

Este é um aplicativo simples para download de vídeos do YouTube utilizando a biblioteca `yt_dlp`. A interface gráfica foi desenvolvida usando `customtkinter`, permitindo que os usuários insiram a URL do vídeo e selecionem o local onde desejam salvar o vídeo baixado.

## Funcionalidades

- **Baixar Vídeos do YouTube**: Insira a URL do vídeo do YouTube e baixe-o no formato MP4.
- **Selecionar Destino de Download**: Escolha a pasta onde o vídeo será salvo.
- **Feedback de Progresso**: A interface exibe o progresso do download, incluindo a porcentagem e o tempo estimado restante.

## Requisitos

Certifique-se de ter os seguintes pacotes instalados antes de executar o programa:

- `yt_dlp`
- `customtkinter`

Você pode instalá-los utilizando o `pip`:

```bash
pip install yt_dlp customtkinter tkinter 
```
## Uso

1. Clone o repositório para sua máquina local.
2. Navegue até o diretório do projeto.
3. Execute o arquivo `main.py`:

```bash
python main.py
```

4. Insira a URL do vídeo do YouTube.
5. Selecione o destino para salvar o vídeo.
6. Clique no botão "Baixar vídeo" e aguarde a conclusão do download.

## Estrutura do Projeto

```
📦 Vídeo Downloader
 ┣ 📂dist
 ┃ ┗ 📜salvar_videos_youtube.exe
 ┣ 📜main.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```

- **`dist/salvar_videos_youtube.exe`**: Executável gerado a partir do script Python.
- **`main.py`**: Código principal do aplicativo.
- **`README.md`**: Documentação do projeto.
- **`requirements.txt`**: Lista de dependências necessárias para executar o projeto.

## Executável

Você pode encontrar o executável na pasta `dist` com o nome `salvar_videos_youtube.exe`. Este executável foi gerado a partir do script `main.py` e permite que o programa seja executado sem a necessidade de Python instalado.

## Contribuição

Se você quiser contribuir com o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```
