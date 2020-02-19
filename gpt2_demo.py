# -*- coding: utf-8 -*-

from flask import Flask, render_template, session, url_for, redirect, request, jsonify
from flask_bootstrap import Bootstrap
import logging
from transformers import GPT2LMHeadModel


async_mode = None
gpt2 = Flask(__name__)
gpt2.config['SECRET_KEY'] = '961018961018'
bootstrap = Bootstrap(gpt2)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-6s %(levelname)-6s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='gpt.log',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
# 设置格式
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
# 告诉handler使用这个格式
console.setFormatter(formatter)
# add the handler to the root logger
# 为root logger添加handler
logging.getLogger('').addHandler(console)

logging.info('begin')

from tokenizations import tokenization_bert
from generate_ import gen

device = "cpu"
tokenizer = tokenization_bert.BertTokenizer(vocab_file='cache/vocab.txt')
model_normal = GPT2LMHeadModel.from_pretrained('model/final_model/')
model_normal.to(device)
model_normal.eval()

model_covi = GPT2LMHeadModel.from_pretrained('model/covi_final_model/')
model_covi.to(device)
model_covi.eval()

def check_contain_chinese(check_str):
    for ch in check_str:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


@gpt2.route('/', methods=['GET', 'POST'])
def home():
    raw = ''
    er = 0
    result = ''
    res_arr = []
    _num = 3
    _len = 50
    _temp = 1.0
    _covi = 0
    # searchForm = SearchForm()
    # if searchForm.submit.data and searchForm.validate_on_submit():
    if request.method == 'POST':
        # print(searchForm.submit.data)
        print('==========')
        raw = request.form['raw_text']
        try:
            _covi = int(request.form['_covi'])
        except:
            _covi = 0
        # _covi=0
        _num = int(request.form['_num'])
        _len = int(request.form['_len'])
        # _temp = float(request.form['_temp'])
        print(raw)
        print(_covi)
        print(_num)
        print(_len)
        if _covi == 1:
            print(11111111)
            model = model_covi
        else:
            model = model_normal
        # print(_temp)
        # if raw == '':
        #     er = 1
        # else:
        er = -1
        res_arr = gen(raw, model, tokenizer, _num, _len, _temp)
        # res_arr = ["# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)",
        #            "# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)",
        #            "# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)",
        #            "# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)",
        #            "# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)",
        #            "# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)",
        #            "# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)",
        #            "# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)# res_arr = gen(raw, model, tokenizer)"
        #            ]
        result = raw + "1234"
        return render_template("home.html", raw=raw, results=result, results_cont=res_arr, error=er, _len=_len, _num=_num, _temp=_temp, _covi=_covi)
    print(er)
    return render_template("home.html", raw=raw, results=result, error=er, _len=_len, _num=_num, _temp=_temp, _covi=_covi)


if __name__ == '__main__':
    gpt2.run(debug=True)
