
import logging

from telegram import __version__ as TG_VER
import base64
import io
from gradio.processing_utils import encode_pil_to_base64
from PIL import Image
import requests


try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update, constants
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


mask_img = encode_pil_to_base64(Image.open(r"test/test_files/eleven17/mask2.png"))

init_images = [
    encode_pil_to_base64(Image.open(r"test/test_files/eleven15/1.png")),

    # encode_pil_to_base64(Image.open(r"test/test_files/eleven12/dot.png")),

    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/bali.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/chestahedron.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/energy.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/fiberhead.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/flowers.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/heart.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/keeper.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/rabbit.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/rust.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs1/unicorn.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/abstract.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/abstracthole.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/animegirl.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/double.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/fiberbody.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/fractalsprout.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/hornygirl.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/ico.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/kubes.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/mindai.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/scaryfeeling.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/scaryfish.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/somethingalikve.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/wavefractal.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs2/wooden.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/breakthrough.jpg")),                                                            
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/cutegirl.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/breakthrough.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/drink.jpg")),                                                            
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/fantasy.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/flowers.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/flyfractal.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/hammer.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/horse.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/inhand.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/innerfractal.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/politics.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/sfractal.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/sky.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/tesla.jpg")),
    # encode_pil_to_base64(Image.open(r"test/test_files/inputs3/thundeer.jpg"))
]

token_ids = [
    # "101",
    "102"
    # "92",
    # "96",
    # "89",
    # "76",
    # "49",
    # "98",
    # "77",
    # "10",
    # "82",
    # "87"
]

idx_curr = 0
idx_max = len(init_images)


sampler_index = "Euler a"
size = 512
steps = 20
cfg_scale = 13
strength = 0.9

locked = False

async def sampler_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global sampler_index
    sampler_index = update.message.text[8:]
    await update.message.reply_text("Sampler " + sampler_index)

async def size_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global size
    size = update.message.text[5:]
    await update.message.reply_text("Size " + size)

async def steps_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global steps
    steps = update.message.text[6:]
    await update.message.reply_text("Steps " + steps)

async def scale_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global cfg_scales
    cfg_scale = update.message.text[6:]
    await update.message.reply_text("Guidance Scale " + cfg_scale)

async def strength_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global strength
    strength = update.message.text[9:]
    await update.message.reply_text("Strength " + strength)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global locked
    if locked == True:
        return
    locked = True

    """Echo the user message."""
    url_img2img = "http://localhost:7860/sdapi/v1/img2img"
    # newFile = await message.effective_attachment.get_file()
    # await newFile.download('file_name')
    # print(newFile)
    # init_images2=[newFile]
    global idx_curr
    simple_img2img = {
        "init_images": [init_images[idx_curr]],
        "resize_mode": 1,
        "denoising_strength": strength,
        "mask": mask_img,
        "mask_blur": 4,
        "inpainting_fill": 2,
        "inpaint_full_res": False,
        "inpaint_full_res_padding": 20,
        "inpainting_mask_invert": 1,
        "prompt": update.message.text,
        "styles": [],
        "seed": -1,
        "subseed": -1,
        "subseed_strength": 0,
        "seed_resize_from_h": -1,
        "seed_resize_from_w": -1,
        "batch_size": 1,
        "n_iter": 1,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "width": size,
        "height": size,
        "restore_faces": False,
        "tiling": False,
        "negative_prompt": "",
        "eta": 0,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 1,
        "override_settings": {},
        "sampler_index": sampler_index,
        "include_init_images": False
    }
    resp = requests.post(url_img2img, json=simple_img2img)
    if (resp.status_code == 200):
        resp_img = resp.json()['images'][0]
        # resp_img = "data:image/;base64,"+resp_img
        # image = image_from_url_text(filedata)
        filedata = base64.decodebytes(resp_img.encode('utf-8'))
        # image = Image.open(io.BytesIO(filedata))
        await update.message.reply_photo(filedata)
        idx_curr += 1
        if (idx_curr == idx_max):
            idx_curr = 0
        galaxy_id = token_ids[idx_curr]
        await update.message.reply_text("Progressors! What springs forth of <a href='https://t.me/galaxyfractals/"+galaxy_id+"'>Galaxy #"+galaxy_id+"</a>?",
            parse_mode=constants.ParseMode.HTML
        )
        locked = False
        # await update.message.reply_text(resp_img)

    # await update.message.reply_photo()


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5423305965:AAFlBSLsNeAIpChb_NX1ooSqpVWUW0m51PI").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("steps", steps_command))
    application.add_handler(CommandHandler("scale", scale_command))
    application.add_handler(CommandHandler("size", size_command))
    application.add_handler(CommandHandler("sampler", sampler_command))
    application.add_handler(CommandHandler("strength", strength_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & (~ filters.COMMAND), echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()