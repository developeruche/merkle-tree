import hashlib

Round = 0

def merkle(hashList):
    global Round
    Round = Round + 1

    if len(hashList) == 1:
        # returning the merkle root
        return hashList[0]

    newHashList = []


    for i in range(0, len(hashList)-1, 2):
        newHashList.append(hash2(hashList[i], hashList[i+1]))
        return merkle(newHashList)


def hash2(first, second):
    first_verse = first.decode('hex')[::-1]
    second_verse = second.decode('hex')[::-1]

    h = hashlib.sha256(hashlib.sha256(first_verse+second_verse).digest()).digest()
    return h[::-1].encode("hex")




# testing the merkle tree algorithm
tx_hashes = [
    "hjksxdcjhsdcnkjhsdkksadk",
    "hjksxdcjhsdcnkjhsdkkssdk",
    "hjksxdcjhsdcnkjhsdkksqdk",
    "hjksxdcjhsdcnkjhsdkksfdk",
    "hjksxdcjhsdcnkjhsdkksbdk",
    "hjksxdcjhsdcnkjhsdkksjdk",
    "hjksxdcjhsdcnkjhsdkkstdk",
    "hjksxdcjhsdcnkjhsdkksedk",
    "hjksxdcjhsdcnkjhsdkkswdk",
    "hjksxdcjhsdcnkjhsdkksldk",
    "hjksxdcjhsdcnkjhsdkksodk",
Round

def merkle(hashLi