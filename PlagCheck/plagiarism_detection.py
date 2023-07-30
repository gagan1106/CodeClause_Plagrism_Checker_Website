import difflib

def plagiarism_check(document):
    # Read the content of the uploaded document
    content = document.read().decode('utf-8')

    # Load a list of reference documents
    reference_documents = ['reference_doc1.txt', 'reference_doc2.txt', 'reference_doc3.txt']

    # Calculate similarity score between the uploaded document and each reference document
    similarity_scores = []
    for ref_doc in reference_documents:
        ref_content = open(ref_doc, 'r').read()
        similarity = difflib.SequenceMatcher(None, content, ref_content).ratio()
        similarity_scores.append(similarity)

    # Check if any similarity score exceeds the threshold
    if max(similarity_scores) >= 0.8:
        return 'Plagiarism detected.'
    else:
        return 'No plagiarism detected.'
