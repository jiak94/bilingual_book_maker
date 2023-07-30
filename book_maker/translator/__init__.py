from book_maker.translator.caiyun_translator import Caiyun
from book_maker.translator.chatgptapi_translator import ChatGPTAPI
from book_maker.translator.deepl_translator import DeepL
from book_maker.translator.deepl_free_translator import DeepLFree
from book_maker.translator.google_translator import Google
from book_maker.translator.gpt3_translator import GPT3
from book_maker.translator.gpt4_translator import GPT4
from book_maker.translator.claude_translator import Claude
from book_maker.translator.gpt4_rewriter import GPT4Rewriter
from book_maker.translator.gpt3_rewriter import GPT3Rewriter

MODEL_DICT = {
    "chatgptapi": ChatGPTAPI,
    "gpt3": GPT3,
    "google": Google,
    "caiyun": Caiyun,
    "deepl": DeepL,
    "deeplfree": DeepLFree,
    "gpt4": GPT4,
    "claude": Claude,
    "gpt4_rewriter": GPT4Rewriter,
    "gpt3_rewriter": GPT3Rewriter,
    # add more here
}
