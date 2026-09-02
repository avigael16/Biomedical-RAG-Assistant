import os 
from config import PDF_UPLOAD_FOLDER, IMAGE_UPLOAD_FOLDER

def save_uploaded_file (uploaded_file,folder):
    #create folder if doesn't existe
    os.makedirs(folder,exist_ok=True)

    #Path 
    file_path =os.path.join(
        folder,
        uploaded_file.name
    )

    #save file

    with open( file_path,"wb") as f:
        f.write(uploaded_file.getbuffer())


    return file_path

def save_uploaded_pdf(uploaded_pdf):

    return save_uploaded_file(
        uploaded_pdf,
        PDF_UPLOAD_FOLDER
    )

def saved_uploaded_image(uploaded_image):

    return saved_uploaded_image(
        uploaded_image,
        IMAGE_UPLOAD_FOLDER
    )