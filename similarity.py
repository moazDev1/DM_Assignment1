# -------------------------------------------------------------------------
# AUTHOR: Moaz
# FILENAME: similarity.py
# SPECIFICATION: Find the most similar documents from cleaned_document.csv
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: 1 hour
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy,
#pandas, or other sklearn modules.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity

documents = []


#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
    if i > 0: #skipping the header
      documents.append (row)
      #print(row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection without applying any transformations, using
# the spaces as your character delimiter.
#--> add your Python code here
docTermMatrix = []


# Extract all distinct words from all documents
distincts = set() # Using set to store distincts values by default and get O(1) finding time
for document in documents:
  words = document[1].split(' ')
  for word in words:
    distincts.add(word)

# Represent each document as a binary vector based on distinct occurrence
for document in documents:
  words = set(document[1].split(' ')) # Using set to get O(1) finding time
  binary_vector = []
  for word in distincts:
    if word in words:
      binary_vector.append(1)
    else:
      binary_vector.append(0)

  docTermMatrix.append(binary_vector)

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here

max_similarity = 0
most_similar_docs = (None, None)

for i in range(len(docTermMatrix)):
  for j in range(i + 1, len(docTermMatrix)): # Avoid redundant comparisons
    similarity = cosine_similarity([docTermMatrix[i]], [docTermMatrix[j]])[0][0]
    if similarity > max_similarity:
      max_similarity = similarity
      most_similar_docs = (i + 1, j + 1) # Convert index to document number

# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here

print(f"The most similar documents are document {most_similar_docs[0]} and document {most_similar_docs[1]} with cosine similarity = {max_similarity}")
