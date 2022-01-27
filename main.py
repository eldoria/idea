import os
from discord.ext import commands
from dotenv import load_dotenv
import gpt_2_simple as gpt2

from transformers import pipeline# , GPT2Tokenizer, GPT2LMHeadModel


# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2LMHeadModel.from_pretrained('gpt2')
# generation = pipeline('text-generation')
translation = pipeline('translation_en_to_fr')

load_dotenv()
bot = commands.Bot(command_prefix='?')


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')


@bot.command(name='p')
async def prediction(ctx, *message: str):
    print(message)
    '''
    text_generated = gpt2.generate(sess,
                  length=25,
                  temperature=0.7,
                  prefix=message,
                  nsamples=1,
                  return_as_list=True
                  )
    for sentence in text_generated.split('.'):
        await ctx.send(translation(sentence)[0]['translation_text'])
    '''

print('Bot prêt')
bot.run(os.getenv("TOKEN"))


