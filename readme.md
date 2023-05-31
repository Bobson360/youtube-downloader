# YouTube Playlist Downloader

Esse é um script Python para baixar vídeos e áudios de uma playlist do YouTube. 

## Recursos

- Baixa vídeos e/ou áudios de uma playlist do YouTube.
- Salva os vídeos e áudios baixados em pastas separadas com o nome da playlist.
- Ignora os arquivos que já foram baixados para evitar downloads duplicados.
- Converte os arquivos de áudio baixados para o formato mp3.
- Permite ao usuário escolher se deseja baixar apenas vídeos, apenas áudios, ou ambos.

## Uso

1. Execute o script Python.
2. Insira a URL da playlist que você deseja baixar.
3. Selecione o que você deseja baixar: 
   - Digite "1" para baixar apenas vídeos.
   - Digite "2" para baixar apenas áudios.
   - Digite "3" para baixar ambos.


### Compilação para um executável com PyInstaller

Caso deseje compilar o script Python para um arquivo executável, você pode usar a biblioteca PyInstaller. 

1. Instale PyInstaller com o pip: `pip install pyinstaller`
2. Navegue até a pasta onde está o arquivo `playlist.py`.
3. Execute o comando a seguir: `pyinstaller --onefile playlist.py`
4. O PyInstaller criará uma pasta chamada `dist`, onde você encontrará o arquivo executável.

Note que este executável é específico para o sistema operacional e a arquitetura do computador onde foi gerado. Para gerar executáveis para outros sistemas ou arquiteturas, você precisará executar o PyInstaller naquela máquina específica.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python: `pytube`, `moviepy`, `pyinstaller`

Para instalar as bibliotecas necessárias, use o seguinte comando: pip install `pytube` `moviepy` `pyinstaller`



## Informações do Projeto

- Autor: Robson Rodrigues
- Data: 29/05/2023
- Links:
  - [GitHub](https://github.com/Bobson360/youtube-downloader)
  - [LinkedIn](https://www.linkedin.com/in/robson-rodrigues-2a973a165/)
- Descrição:
  - Insira uma playlist válida e pública com os vídeos de deseja baixar.
  - O programa pode criar duas pastas, uma para vídeo e outra para áudio, a playlist.
  - Escolha o que deseja baixar, 1 para vídeo, 2 para áudio e 3 para ambos.
  - Caso o item já exista no diretório vídeo|áudio, não será baixado novamente.

## Aviso Legal

Este código é destinado para fins educacionais e pessoais apenas, sem intenção de causar danos. Baixar conteúdo protegido por direitos autorais pode ser ilegal em sua jurisdição. Este código não incentiva ou endossa tal comportamento, e não pode ser usado para tais fins. O autor não é responsável por qualquer uso ou mau uso deste código.

Release: [Baixar arquivo](https://github.com/Bobson360/youtube-downloader/raw/master/release/youtube%20downloader%200.1.1.zip)
