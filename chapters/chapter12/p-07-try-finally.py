def main():
    try:
        a = int(input("enter your number"))
        print(a)



    except Exception as e:
        print(e)

    finally:
        print("I am inside finally")

main()