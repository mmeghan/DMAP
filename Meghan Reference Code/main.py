from multiprocessing import Pool, cpu_count
from functools import partial
from Downloader import zip_downloader
from ClinicalAnnotations import ReadClinicalAnnotations
from ClinicalEvidence import ReadClinicalEvidence
from APIfetch import callClinicalAnnotation, callHaplotype
from GetRS import files
from WriteJson import writeJson

gene_drug = {}
gene_variant = {}
id_url = {}

def main():
    '''
    the goal of this function is to call all of the functions in the correct order and run the overall program 

    '''
    entries = []
    data = []
    PharmGKB_url = ["https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations.zip"]
    pool = Pool(cpu_count())
    download_func = partial(zip_downloader, filePath = 'output/')
    results = pool.map(download_func, PharmGKB_url)
    pool.close()
    pool.join()

    f = open('output/problemfiles.txt', 'r+')
    f.truncate(0)
    f. close()

    ReadClinicalEvidence(data, id_url)
    ReadClinicalAnnotations(entries, gene_drug, gene_variant)
    callClinicalAnnotation(gene_variant, gene_drug)
    callHaplotype(gene_variant)

    with open('output/problemfiles.txt', 'w+') as problems:
        for gene, description in files.items():
            problems.write('%s:\n%s\n' % (gene, description))
    problems.close()
    
    writeJson(gene_variant, gene_drug, id_url)

    print("Check problemfiles.txt in the output folder for any cases of missing information")
if __name__ == "__main__":
    main()
