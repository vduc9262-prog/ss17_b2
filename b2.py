product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]


def display_product(products):

    print("\n--- DANH SÁCH TEM NHÃN ---")

    for product in products:

        data = product.split("-")

        if len(data) != 4:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")
            continue

        product_id, name, price, rating = data

        if not price.isdigit():
            print(f"Bỏ qua sản phẩm {product_id} do giá không hợp lệ")
            continue

        info = {
            "product_id": product_id,
            "name": name,
            "price": f"{int(price):,}",
            "rating": rating
        }

        template = (
            "Mã: {product_id:<10} | "
            "Tên: {name:<20} | "
            "Giá: {price:<10} VND | "
            "Rating: {rating}*"
        )

        print(template.format_map(info))


def sort_key(product):

    data = product.split("-")

    if len(data) != 4:
        return (999, 999999)

    if not data[2].isdigit():
        return (999, 999999)

    rating = float(data[3])
    price = int(data[2])

    return (-rating, price)


def sort_products():

    product_list.sort(key=sort_key)

    print("\n--- SẮP XẾP SẢN PHẨM ---")

    for i, product in enumerate(product_list, 1):
        print(f"{i}. {product}")


def calculate_total():

    total = 0

    for product in product_list:

        data = product.split("-")

        if len(data) != 4:
            continue

        if not data[2].isdigit():
            continue

        total += int(data[2])

    return total


def main():

    while True:

        choice = input("""
============= E-COMMERCE ANALYTICS =============

1. Hiển thị tem nhãn sản phẩm
2. Sắp xếp sản phẩm thông minh
3. Tính tổng giá trị kho hàng
4. Đóng hệ thống

================================================
Chọn chức năng (1-4): """)

        if choice == "1":

            display_product(product_list)

        elif choice == "2":

            sort_products()

        elif choice == "3":

            total = calculate_total()

            print("\n--- TỔNG GIÁ TRỊ KHO ---")
            print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND")

        elif choice == "4":

            print("Đóng hệ thống...")
            break

        else:

            print("Lựa chọn không hợp lệ!")


main()