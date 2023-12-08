import gdown
import os
from subprocess import call
from IPython.display import clear_output

class model_downloads:
  def checkpoint_dl(self, model_name, MODEL_LINK):
    final_model_name = f'/content/drive/MyDrive/sd/stable-diffusion-webui/models/Stable-diffusion/{model_name}.safetensors'
    # model='/content/gdrive/MyDrive/sd/stable-diffusion-webui/models/Stable-diffusion/model.safetensors'

    if os.path.exists(final_model_name):
        call('rm '+final_model_name, shell=True)

    # if os.path.exists(model):
    #     call('rm '+model, shell=True)

    gdown.download(url=MODEL_LINK, output=final_model_name, quiet=False, fuzzy=True)

    if os.path.exists(final_model_name): # and os.path.getsize(lora) > 1810671599:
        # call(
        #     'mv ' + model + ' ' + final_model_name,
        #     shell=True
        # )

        clear_output()
        print('[1;32mModel downloaded.')
    else:
        print('[1;31mWrong link, check that the link is valid')

    try:
        final_model_name
    except:
        final_model_name="/content/drive/MyDrive/sd/stable-diffusion-webui/models/Stable-diffusion/"

    return final_model_name

  def loradl(self, folder, lora_name, LORA_LINK, lycoris=False):
    if folder == "addnet":
      lora=f'/content/drive/MyDrive/sd/stable-diffusion-webui/extensions/sd-webui-additional-networks/models/lora/{lora_name}.safetensors'
    elif folder == "models" and lycoris:
      lora=f'/content/drive/MyDrive/sd/stable-diffusion-webui/models/LyCORIS/{lora_name}.safetensors'
    else:
      lora=f'/content/drive/MyDrive/sd/stable-diffusion-webui/models/Lora/{lora_name}.safetensors'

    if os.path.exists(lora):
      call('rm '+lora, shell=True)

    gdown.download(url=LORA_LINK, output=lora, quiet=False, fuzzy=True)

    # print(os.path.getsize(lora))
    # print(os.path.exists(lora))

    if os.path.exists(lora): # and os.path.getsize(lora) > 1810671599:
      clear_output()
      print('[1;32mLora downloaded.')
    else:
      print('[1;31mWrong link, check that the link is valid')

    try:
      lora
    except:
      lora="/content/drive/MyDrive/sd/stable-diffusion-webui/models/Lora/"

    return lora

  def controlnet_dl(self, controlnet_name, CONTROLNET_LINK):
      controlnet = f'/content/drive/MyDrive/sd/stable-diffusion-webui/extensions/sd-webui-controlnet/models/{controlnet_name}.safetensors'
  
      if os.path.exists(controlnet):
          call('rm ' + controlnet, shell=True)
  
      gdown.download(url=CONTROLNET_LINK, output=controlnet, quiet=False, fuzzy=True)
  
      if os.path.exists(controlnet):
          clear_output()
          print('\x1b[1;32mControlNet downloaded.')
      else:
          print('\x1b[1;31mWrong link, check that the link is valid')
  
      try:
          controlnet
      except:
          controlnet = "/content/drive/MyDrive/sd/stable-diffusion-webui/extensions/sd-webui-additional-networks/models/controlnet"
  
      return controlnet

# Instantiate
manage_models = model_downloads()
