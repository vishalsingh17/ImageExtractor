import hashlib
 
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()