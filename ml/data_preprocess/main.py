import  classifier

def main():

    clf = classifier.train()
    classifier.test(clf)

if __name__ == "__main__":
    main()