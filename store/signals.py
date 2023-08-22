from datetime import  datetime

def save_area_volume(sender,instance,created,**kwargs):
    try:
        if created:
            model_created = instance.__class__.__name__
            instance.area = instance.find_area()
            instance.volume = instance.find_volume()
            instance.last_updated = datetime.now()
            instance.save()
    except Exception as E:
        pass