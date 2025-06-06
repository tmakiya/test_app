import os
from dash import Dash, html, dcc, Input, Output
import pathlib

app = Dash(__name__)
server = app.server

CONTENT_DIR = pathlib.Path('content')
ASSETS_DIR = pathlib.Path('assets')

app.layout = html.Div([
    html.H1('製造業向けコンテンツ配信プラットフォーム'),
    dcc.Tabs(id='tabs', value='video', children=[
        dcc.Tab(label='動画', value='video'),
        dcc.Tab(label='音声', value='audio'),
        dcc.Tab(label='テキスト', value='text'),
        dcc.Tab(label='スライド', value='slide'),
    ]),
    html.Div(id='content-area')
])

@app.callback(Output('content-area', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'video':
        video_path = ASSETS_DIR / 'sample_video.mp4'
        if video_path.exists() and video_path.stat().st_size > 0:
            return html.Video(src='/assets/sample_video.mp4', controls=True, style={'width': '100%'})
        return html.Div('動画ファイルをassetsフォルダに配置してください。')
    elif tab == 'audio':
        audio_path = ASSETS_DIR / 'sample_audio.wav'
        if audio_path.exists():
            return html.Audio(src='/assets/sample_audio.wav', controls=True)
        return html.Div('音声ファイルをassetsフォルダに配置してください。')
    elif tab == 'text':
        text_path = CONTENT_DIR / 'sample_text.md'
        if text_path.exists():
            with open(text_path, 'r', encoding='utf-8') as f:
                text = f.read()
            return dcc.Markdown(text)
        return html.Div('テキストファイルが見つかりません。')
    elif tab == 'slide':
        slide_path = ASSETS_DIR / 'sample_slide.png'
        if slide_path.exists():
            return html.Img(src='/assets/sample_slide.png', style={'max-width': '100%'})
        return html.Div('スライドファイルをassetsフォルダに配置してください。')
    return html.Div()

if __name__ == '__main__':
    app.run_server(debug=True)
