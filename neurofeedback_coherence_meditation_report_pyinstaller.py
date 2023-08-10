import os
import sys

# Module multiprocessing is organized differently in Python 3.4+
try:
    # Python 3.4+
    if sys.platform.startswith("win"):
        import multiprocessing.popen_spawn_win32 as forking
    else:
        import multiprocessing.popen_fork as forking
except ImportError:
    import multiprocessing.forking as forking

if sys.platform.startswith("win"):
    # First define a modified version of Popen.
    class _Popen(forking.Popen):
        def __init__(self, *args, **kw):
            if hasattr(sys, "frozen"):
                # We have to set original _MEIPASS2 value from sys._MEIPASS
                # to get --onefile mode working.
                os.putenv("_MEIPASS2", sys._MEIPASS)
            try:
                super(_Popen, self).__init__(*args, **kw)
            finally:
                if hasattr(sys, "frozen"):
                    # On some platforms (e.g. AIX) 'os.unsetenv()' is not
                    # available. In those cases we cannot delete the variable
                    # but only set it to the empty string. The bootloader
                    # can handle this case.
                    if hasattr(os, "unsetenv"):
                        os.unsetenv("_MEIPASS2")
                    else:
                        os.putenv("_MEIPASS2", "")

    # Second override 'Popen' class with our modified version.
    forking.Popen = _Popen

import multiprocessing

import re
import sys

import argparse
import gradio as gr
_image_output0 = None
_image_output1 = None
_image_output2 = None
_image_output3 = None
_image_output4 = None
_text_output0 = None
_text_output1 = None
_text_output2 = None
def update0(image_input0, text_input00):
    global _image_output0
#    print('_image_output0: ', _image_output0)
#    print('image_input0: ', image_input0)
    if (_image_output0 is None) or ((image_input0 is not None) and (image_input0.any())):
        _image_output0 = image_input0
    if not (_image_output0 is None):
        return _image_output0
def update1(image_input1, text_input01):
    global _image_output1
#    print('_image_output1: ', _image_output1)
#    print('image_input1: ', image_input1)
    if (_image_output1 is None) or ((image_input1 is not None) and (image_input1.any())):
        _image_output1 = image_input1
    if not (_image_output1 is None):
        return _image_output1
def update2(image_input2, text_input02):
    global _image_output2
#    print('_image_output2: ', _image_output2)
#    print('image_input2: ', image_input2)
    if (_image_output2 is None) or ((image_input2 is not None) and (image_input2.any())):
        _image_output2 = image_input2
    if not (_image_output2 is None):
        return _image_output2
def update3(image_input3, text_input03):
    global _image_output3
#    print('_image_output3: ', _image_output3)
#    print('image_input3: ', image_input3)
    if (_image_output3 is None) or ((image_input3 is not None) and (image_input3.any())):
        _image_output3 = image_input3
    if not (_image_output3 is None):
        return _image_output3
def update4(image_input4, text_input04):
    global _image_output4
#    print('_image_output4: ', _image_output4)
#    print('image_input4: ', image_input4)
    if (_image_output4 is None) or ((image_input4 is not None) and (image_input4.any())):
        _image_output4 = image_input4
    if not (_image_output4 is None):
        return _image_output4
def update5(text_input0, text_input1, text_input2):
    global _text_output0
    global _text_output1
    global _text_output2
    if (not(text_input0 == "")) or (_text_output0 is None):
        _text_output0 = text_input0
    if (not(text_input1 == "")) or (_text_output1 is None):
        _text_output1 = text_input1
    if (not(text_input2 == "")) or (_text_output2 is None):
        _text_output2 = text_input2
    return [_text_output0, _text_output1, _text_output2]
    
def ui_full(launch_kwargs):
    
  with gr.Blocks() as demo:
    with gr.Tab("Meditation Report"):
        with gr.Row():
            with gr.Column():
                image_input2 = gr.Image(visible=False)
                text_input02 = gr.Textbox("{}", show_label=False, visible=False)
                image_output2 = gr.Image(shape=[400,400]).style(height=400)
                gr.Markdown("Alpha")
        with gr.Row():
            text_output000 = gr.Textbox("Average frontal left (Fp1, F7, F3) to right (Fp2, F8, F4)", show_label=False).style(height=42)
            text_input0 = gr.Textbox("", show_label=False, visible=False)
            text_output0 = gr.Textbox("", show_label=False)
        with gr.Row():
            text_output001 = gr.Textbox("Average parietal left (C3, P3, T5) to right (C4, P4, T6)", show_label=False).style(height=42)
            text_input1 = gr.Textbox("", show_label=False, visible=False)
            text_output1 = gr.Textbox("", show_label=False)
        with gr.Row():
            text_output002 = gr.Textbox("Average front (Fp1, Fp2, F3, F4, F7, F8, FZ) to back (PZ, P3, P4, O1, O2)", show_label=False).style(height=42)
            text_input2 = gr.Textbox("", show_label=False, visible=False)
            text_output2 = gr.Textbox("", show_label=False)
        with gr.Row():
            with gr.Column():
                image_input0 = gr.Image(visible=False)
                text_input00 = gr.Textbox("{}", show_label=False, visible=False)
                image_output0 = gr.Image(shape=[200,200]).style(height=200)
                gr.Markdown("Delta")
            with gr.Column():
                image_input1 = gr.Image(visible=False)
                text_input01 = gr.Textbox("{}", show_label=False, visible=False)
                image_output1 = gr.Image(shape=[200,200]).style(height=200)
                gr.Markdown("Theta")
            with gr.Column():
                image_input3 = gr.Image(visible=False)
                text_input03 = gr.Textbox("{}", show_label=False, visible=False)
                image_output3 = gr.Image(shape=[200,200]).style(height=200)
                gr.Markdown("Beta")
            with gr.Column():
                image_input4 = gr.Image(visible=False)
                text_input04 = gr.Textbox("{}", show_label=False, visible=False)
                image_output4 = gr.Image(shape=[200,200]).style(height=200)
                gr.Markdown("Gamma")
    demo.load(update0, [image_input0, text_input00], [image_output0], every=1)
    demo.load(update1, [image_input1, text_input01], [image_output1], every=1)
    demo.load(update2, [image_input2, text_input02], [image_output2], every=1)
    demo.load(update3, [image_input3, text_input03], [image_output3], every=1)
    demo.load(update4, [image_input4, text_input04], [image_output4], every=1)
    demo.load(update5, [text_input0, text_input1, text_input2], [text_output0, text_output1, text_output2], every=1)
#    demo.load(update5, [text_output0, text_output1, text_output2, text_input0, text_input1, text_input2], [text_output0, text_output1, text_output2, text_input0, text_input1, text_input2], every=1)
    image_input_btn0 = gr.Button("Delta", visible=False)
    image_input_btn1 = gr.Button("Theta", visible=False)
    image_input_btn2 = gr.Button("Alpha", visible=False)
    image_input_btn3 = gr.Button("Beta", visible=False)
    image_input_btn4 = gr.Button("Gamma", visible=False)
    text_btn = gr.Button("Average", visible=False)
    image_output0 = image_input_btn0.click(update0, [image_input0, text_input00], [image_output0])
    image_output1 = image_input_btn1.click(update1, [image_input1, text_input01], [image_output1])
    image_output2 = image_input_btn2.click(update2, [image_input2, text_input02], [image_output2])
    image_output3 = image_input_btn3.click(update3, [image_input3, text_input03], [image_output3])
    image_output4 = image_input_btn4.click(update4, [image_input4, text_input04], [image_output4])
    text_btn.click(update5, [text_input0, text_input1, text_input2], [text_output0, text_output1, text_output2])


  #demo.launch()
  demo.queue(concurrency_count=10, max_size=50).launch(**launch_kwargs)

if __name__ == "__main__":
    multiprocessing.freeze_support()
#    sys.argv[0] = re.sub(r"(-script\.pyw|\.exe)?$", "", sys.argv[0])
#    sys.exit(main())

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--listen',
        type=str,
        default='0.0.0.0' if 'SPACE_ID' in os.environ else '127.0.0.1',
        help='IP to listen on for connections to Gradio',
    )
    parser.add_argument(
        '--username', type=str, default='', help='Username for authentication'
    )
    parser.add_argument(
        '--password', type=str, default='', help='Password for authentication'
    )
    parser.add_argument(
        '--server_port',
        type=int,
        default=0,
        help='Port to run the server listener on',
    )
    parser.add_argument(
        '--inbrowser', action='store_true', help='Open in browser'
    )
    parser.add_argument(
        '--share', action='store_true', help='Share the gradio UI'
    )

    args = parser.parse_args()

    launch_kwargs = {}
    launch_kwargs['server_name'] = args.listen

    if args.username and args.password:
        launch_kwargs['auth'] = (args.username, args.password)
    if args.server_port:
        launch_kwargs['server_port'] = args.server_port
    if args.inbrowser:
        launch_kwargs['inbrowser'] = args.inbrowser
    if args.share:
        launch_kwargs['share'] = args.share

    # Show the interface
    ui_full(launch_kwargs)


