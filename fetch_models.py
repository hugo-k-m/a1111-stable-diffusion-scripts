import gdown
import os
from subprocess import call
from IPython.display import clear_output

class model_downloads:
    def checkpoint_dl(self, model_name, MODEL_LINK):
        final_model_name = f'/notebooks/sd/stable-diffusion-webui/models/Stable-diffusion/{model_name}.safetensors'
        model='/notebooks/sd/stable-diffusion-webui/models/Stable-diffusion/model.safetensors'

        if os.path.exists(final_model_name):
            call('rm '+final_model_name, shell=True)

        if os.path.exists(model):
            call('rm '+model, shell=True)

        gdown.download(url=MODEL_LINK, output=model, quiet=False, fuzzy=True)

        if os.path.exists(model):
            call(
                'mv ' + model + ' ' + final_model_name,
                shell=True
            )

            clear_output()
            print('[1;32mModel downloaded.')
        else:
            print('[1;31mWrong link, check that the link is valid')

        try:
            model
        except:
            model="/notebooks/sd/stable-diffusion-webui/models/Stable-diffusion"

        return model

    def lora_dl(self, lora_name, LORA_LINK):
        lora=f'/notebooks/sd/stable-diffusion-webui/extensions/sd-webui-additional-networks/models/lora/{lora_name}.safetensors'

        if os.path.exists(lora):
            call('rm '+lora, shell=True)

        gdown.download(url=LORA_LINK, output=lora, quiet=False, fuzzy=True)

        if os.path.exists(lora):
            clear_output()
            print('[1;32mLora downloaded.')
        else:
            print('[1;31mWrong link, check that the link is valid')

        try:
            lora
        except:
            lora="/notebooks/sd/stable-diffusion-webui/extensions/sd-webui-additional-networks/models/lora"

        return lora


    def vae_dl(self, vae_name, VAE_LINK):
        vae=f'/notebooks/sd/stable-diffusion-webui/models/VAE/{vae_name}.safetensors'

        if os.path.exists(vae):
            call('rm '+vae, shell=True)

        gdown.download(url=VAE_LINK, output=vae, quiet=False, fuzzy=True)

        if os.path.exists(vae):
            clear_output()
            print('[1;32mVAE downloaded.')
        else:
            print('[1;31mWrong link, check that the link is valid')

        try:
            vae
        except:
            vae="/notebooks/sd/stable-diffusion-webui/models/VAE"

        return vae
