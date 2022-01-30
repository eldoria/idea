from discord.ext import commands
import gpt_2_simple as gpt2

bot = commands.Bot(command_prefix='?')


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')


@bot.command(name='p')
async def prediction(ctx, *message: str):
    message = ' '.join(message)
    text_generated = gpt2.generate(sess,
                                   length=250,
                                   temperature=0.7,
                                   prefix=message,
                                   nsamples=1,
                                   return_as_list=True
                                   )[0]
    await ctx.send(text_generated)

print('Bot prêt')
bot.run('OTE3MDIxMTYyMjIxOTk4MDkw.Yayogg.zuYDHvvG68QKThE7B-2SZ9IeyNw')


