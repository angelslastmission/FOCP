staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}


combined = staff.union(managers)

common_members = staff.intersection(managers)

staff_only = staff.difference(managers)

unique_members = staff.symmetric_difference(managers)
