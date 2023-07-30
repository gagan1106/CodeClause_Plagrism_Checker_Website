import difflib
import random
import string

def generate_reference_documents(num_docs):
    reference_documents = []
    for i in range(num_docs):
        content = ''.join(random.choices(string.ascii_lowercase, k=100))
        filename = f'reference_doc{i + 1}.txt'
        with open(filename, 'w') as file:
            file.write(content)
        reference_documents.append(filename)
    return reference_documents

def plagiarism_check(document):
    content = document.read().decode('utf-8')

    reference_documents = generate_reference_documents(5)

    similarity_scores = []
    for ref_doc in reference_documents:
        ref_content = open(ref_doc, 'r').read()
        similarity = difflib.SequenceMatcher(None, content, ref_content).ratio()
        similarity_scores.append(similarity)

    if max(similarity_scores) >= 0.8:
        return 'Plagiarism detected.'
    else:
        return 'No plagiarism detected.'
