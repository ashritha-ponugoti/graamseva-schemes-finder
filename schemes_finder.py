schemes = [
    {
        "name": "PM Kisan Samman Nidhi",
        "desc": "Rs6000 per year for farmer families paid in 3 parts.",
        "cat": "Agriculture",
        "min_age": 18, "max_age": 100,
        "max_income": 200000,
        "jobs": ["farmer"],
        "contact": "Call 155261"
    },
    {
        "name": "Indira Gandhi Old Age Pension",
        "desc": "Monthly pension of Rs200 to Rs500 for elderly people below poverty line.",
        "cat": "Pension",
        "min_age": 60, "max_age": 100,
        "max_income": 100000,
        "jobs": ["farmer", "laborer", "unemployed", "retired"],
        "contact": "Go to nearest Gram Panchayat office"
    },
    {
        "name": "Ayushman Bharat",
        "desc": "Free hospital treatment upto Rs5 lakh per year.",
        "cat": "Health",
        "min_age": 0, "max_age": 100,
        "max_income": 200000,
        "jobs": ["farmer", "laborer", "unemployed", "retired", "other"],
        "contact": "Call 14555"
    },
    {
        "name": "PM Ujjwala Yojana",
        "desc": "Free LPG gas connection for women from low income families.",
        "cat": "Women",
        "min_age": 18, "max_age": 100,
        "max_income": 150000,
        "jobs": ["farmer", "laborer", "unemployed", "other"],
        "gender": "female",
        "contact": "Visit nearest LPG gas dealer"
    },
    {
        "name": "Senior Citizen Savings Scheme",
        "desc": "Special savings account for senior citizens with 8.2 percent interest per year.",
        "cat": "Finance",
        "min_age": 60, "max_age": 100,
        "max_income": 9999999,
        "jobs": ["farmer", "laborer", "unemployed", "retired", "other"],
        "contact": "Go to Post Office or SBI bank"
    },
    {
        "name": "PM Fasal Bima Yojana",
        "desc": "Insurance for farmers if crops are damaged due to floods, drought or pests.",
        "cat": "Agriculture",
        "min_age": 18, "max_age": 100,
        "max_income": 9999999,
        "jobs": ["farmer"],
        "contact": "Visit nearest bank branch"
    },
    {
        "name": "MGNREGA",
        "desc": "Guaranteed 100 days of work per year for people in rural areas.",
        "cat": "Employment",
        "min_age": 18, "max_age": 100,
        "max_income": 150000,
        "jobs": ["farmer", "laborer", "unemployed"],
        "contact": "Go to Gram Panchayat office"
    },
    {
        "name": "PM Awas Yojana Rural",
        "desc": "Rs1.2 lakh to help build a proper house in rural areas.",
        "cat": "Housing",
        "min_age": 18, "max_age": 100,
        "max_income": 200000,
        "jobs": ["farmer", "laborer", "unemployed", "retired", "other"],
        "contact": "Visit Block Development Office"
    },
    {
        "name": "Atal Pension Yojana",
        "desc": "Get Rs1000 to Rs5000 pension every month after turning 60.",
        "cat": "Pension",
        "min_age": 18, "max_age": 40,
        "max_income": 9999999,
        "jobs": ["farmer", "laborer", "other"],
        "contact": "Visit any bank or post office"
    },
    {
        "name": "National Social Assistance Programme",
        "desc": "Monthly financial help for poor elderly people, widows and disabled persons.",
        "cat": "Social",
        "min_age": 40, "max_age": 100,
        "max_income": 100000,
        "jobs": ["farmer", "laborer", "unemployed", "retired", "other"],
        "contact": "Visit District Social Welfare Office"
    },
]


def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 1 <= age <= 110:
                return age
            else:
                print("Please enter a valid age between 1 and 110")
        except ValueError:
            print("Age should be a number, try again")


def get_gender():
    while True:
        print("Gender:")
        print("1. Male")
        print("2. Female")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            return "male"
        elif choice == "2":
            return "female"
        else:
            print("Please enter 1 or 2 only")


def get_occupation():
    options = ["farmer", "laborer", "retired", "unemployed", "other"]
    while True:
        print("Occupation:")
        for i, o in enumerate(options, 1):
            print(f"{i}. {o.capitalize()}")
        try:
            ch = int(input("Enter number: "))
            if 1 <= ch <= len(options):
                return options[ch - 1]
            else:
                print("Enter a number from the list")
        except ValueError:
            print("Please enter a number")


def get_income():
    while True:
        print("Yearly household income:")
        print("1. Less than Rs1 lakh")
        print("2. Rs1 lakh to Rs2 lakh")
        print("3. More than Rs2 lakh")
        ch = input("Enter 1, 2 or 3: ")
        if ch == "1":
            return 80000
        elif ch == "2":
            return 150000
        elif ch == "3":
            return 300000
        else:
            print("Enter 1, 2 or 3 only")


def find_schemes(age, gender, occupation, income):
    matched = []
    for s in schemes:
        if age < s["min_age"] or age > s["max_age"]:
            continue
        if income > s["max_income"]:
            continue
        if occupation not in s["jobs"]:
            continue
        if "gender" in s and s["gender"] != gender:
            continue
        matched.append(s)
    return matched


def show_results(matched):
    print("\n" + "="*45)
    if len(matched) == 0:
        print("Sorry, no schemes found for your details.")
        print("You can visit the nearest Gram Panchayat")
        print("office for more help.")
        return

    print(f"Good news! You may qualify for {len(matched)} scheme(s):")
    print("="*45)

    for i, s in enumerate(matched, 1):
        print(f"\n{i}. {s['name']}")
        print(f"   Category : {s['cat']}")
        print(f"   Benefit  : {s['desc']}")
        print(f"   Apply at : {s['contact']}")

    print("\n" + "="*45)
    print("Remember to carry your Aadhaar card")
    print("when you go to apply for any scheme.")
    print("="*45)


def main():
    print("="*45)
    print("  Government Schemes Finder")
    print("  Helping village families know their rights")
    print("="*45)

    while True:
        print()
        age = get_age()
        gender = get_gender()
        occupation = get_occupation()
        income = get_income()

        matched = find_schemes(age, gender, occupation, income)
        show_results(matched)

        print()
        again = input("Search for someone else? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using this tool.")
            print("Please share it with people who need it.")
            break


main()
