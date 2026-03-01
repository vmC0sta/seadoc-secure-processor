from fastapi import FastAPI, UploadFile, File, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from fastapi.responses import FileResponse
import subprocess
import img2pdf
import io

app = FastAPI(title="SeaDoc API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "SeaDoc Backend is running on WSL"}

@app.post("/convert/jpg-to-pdf", summary="JPG para PDF")
async def jpg_to_pdf(file: UploadFile = File(...)):
    img_data = await file.read()
    
    pdf_bytes = img2pdf.convert(img_data)
    
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={file.filename.split('.')[0]}.pdf"}
    )
    
@app.post("/convert/word-to-pdf", summary="Word para PDF")
async def word_to_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(('.doc', '.docx')):
        raise HTTPException(status_code=400, detail="Arquivo precisa ser Word (.doc ou .docx)")

    input_path = f"/tmp/{file.filename}"
    output_dir = "/tmp"
    
    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())
    
    try:
        subprocess.run([
            'lowriter', '--headless', '--convert-to', 'pdf', 
            '--outdir', output_dir, input_path
        ], check=True)
        
        pdf_filename = file.filename.rsplit('.', 1)[0] + ".pdf"
        pdf_path = f"{output_dir}/{pdf_filename}"
        
        return FileResponse(
            path=pdf_path, 
            filename=pdf_filename, 
            media_type='application/pdf'
        )
    except Exception as e:
        return {"error": str(e)}

@app.post("/convert/excel-to-pdf", summary="Excel para PDF")
async def excel_to_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(('.xls', '.xlsx', '.ods')):
        raise HTTPException(status_code=400, detail="Arquivo precisa ser Excel (.xlsx ou .xls)")

    input_path = f"/tmp/{file.filename}"
    output_dir = "/tmp"
    
    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())
    
    try:
        subprocess.run([
            'libreoffice', '--headless', '--convert-to', 'pdf', 
            '--outdir', output_dir, input_path
        ], check=True)
        
        pdf_filename = file.filename.rsplit('.', 1)[0] + ".pdf"
        pdf_path = f"{output_dir}/{pdf_filename}"
        
        return FileResponse(
            path=pdf_path, 
            filename=pdf_filename, 
            media_type='application/pdf'
        )
    except Exception as e:
        return {"error": str(e)}