# Giới Thiệu 

Trong phần nội dung này, sẽ chứa những lý thuyết cơ bản về Python và các thư viện Python thường được sử dụng trong khoa học dữ liệu. 

Bảng tổng kết các kiến thức cơ bản trong Python [tải xuống tại đây](https://github.com/thanhhff/AIVN-Machine-Learning/blob/master/Python/Python3_reference_cheat_sheet.pdf)

<img src="https://imgur.com/1hMqrPZ.png">

# Hướng dẫn sử dụng PyCharm 
### Mục Lục 
[I. Mở đầu](#Modau)

[II. Hướng dẫn cài đặt](#Caidat)
- [1. Download PyCharm](#Download)
- [2. Cài đặt chi tiết](#Huongdancaidat)

[III. Hướng dẫn nâng cấp lên phiên bản Professional miễn phí](#Uppro)

[IV. Hướng dẫn thực thi File và Debug trên PyCharm](#Thucthi_debug)
- [1. Thực thi File](#Thucthi)
- [2. Debug](#Debug)

[Tổng Kết](#Tongket)

=====================================
<a name="Modau"></a>
## I. Mở đầu 
PyCharm phát triển bởi JetBrains. PyCharm cung cấp nhiều tính năng thông minh như bộ code completion, dễ dàng điều hướng và kiểm tra lỗi. IDE này có thể tự động thụt lề, phát hiện văn bản trùng lặp và kiểm tra lỗi. Ngoài ra PyCharm có các tính năng tìm kiếm mã nguồn thông minh để tìm kiếm từng từ một trong nháy mắt. 
Hiện tại PyCharm có 2 phiên bản:
- Phiên bản Professional: đầy đủ tất cả các tính năng, hỗ trợ Python Web với HTML, JS, và SQL. Mức giá hiện tại 199$ / năm đầu tiên.
- Phiên bản Community: hỗ trợ Python development. **`Miễn phí`**

<a name="Caidat"></a>
## II. Hướng dẫn cài đặt 
<a name="Download"></a>
### 1. Download PyCharm
- Truy cập vào trang download trên trang chủ Jetbrains: https://www.jetbrains.com/pycharm/download/
- Lựa chọn phiên bản download phù hợp. (Phiên bản Community cũng đã đầy đủ các tính năng hỗ trợ code Python)
- Mình sẽ hướng dẫn các bạn nâng cấp lên phiên bản Professional **`Miễn phí`** [tại đây](#Uppro).
<img src="https://i.imgur.com/H58ZEom.png">

<a name="Huongdancaidat"></a>
### 2. Cài đặt chi tiết 
- Các bạn truy cập vào liên kết YouTube bên dưới đây để xem chi tiết phần cài đặt: 
- Tác giả **`Than Trieu`**: https://www.youtube.com/watch?v=Z2q7V3ZIghY 

<a name="Uppro"></a>
## III. Hướng dẫn nâng cấp lên phiên bản Professional miễn phí
- Đối với các bạn là học sinh / sinh viên / nghiên cứu sinh / giảng viên sẽ được Jetbrains hỗ trợ nâng cấp lên phiên bản Professional miễn phí.
- Nâng cấp tài khoản lên Pro, các bạn có thể sử dụng miễn phí hơn 15 IDE với đầy đủ chức năng của Jetbrains như: PyCharm, PhpStorm, WebStorm...
- Chú ý: các bạn nên có email của nhà trường để việc nâng cấp dễ dàng hơn.
- Cách nâng cấp:
  - Đầu tiên các bạn truy cập: https://www.jetbrains.com/student/ 
  - Nhấn nút "Apply Now" để tiến hành nâng cấp.
  - Các bạn điền đầy đủ thông tin của các bạn như mình bên dưới (mình sử dụng Email nhà trường cấp).
  - Ngoài ra các bạn có thể Apply thông qua: ISIC/ITIC MEMBERSHIP, GITHUB, ...
  
  <img src="https://i.imgur.com/hlZCWwQ.png">
  
  - Sau đó nhấn "APPLY FOR FREE PRODUCTS". Khi này sẽ có email xác thực gửi đến email đăng ký của bạn.
  - Các bạn "Confirm Request" và đồng ý điều khoản của Jetbrains sẽ được nâng cấp lên phiên bản Professional.
  - Nếu các bạn chưa có tài khoản thì sau khi đồng ý điều khoản sẽ tạo tài khoản mới.
  - Sau đó tài khoản của các bạn sẽ được nâng lên phiên bản Pro, có hiệu lực 1 năm kể từ ngày đăng ký. Sau khi hết hạn các bạn có thể đăng ký mới.
   
   <img src="https://i.imgur.com/ZrzCsrU.png">

- Các bạn download phiên bản Professional về máy và đăng nhập bằng tài khoản bạn đã tạo. 
- Sau khi đăng nhập thành công, khi khởi động phần mềm sẽ có thêm dòng "Licensed to..." là bạn đã thành công nâng cấp lên phiên bản Pro.

    <img src="https://i.imgur.com/DbeN6gu.png">

<a name="Thucthi_debug"></a>
## IV. Hướng dẫn thực thi và Debug trên PyCharm
<a name="Thucthi"></a>
### 1. Thực thi File 
- Sau khi viết xong chương trình, các bạn chọn **`Run`** trên thanh công cụ và ấn **`Run`** (hoặc phím tắt: **`Control + Option + R`** đối với MacOS - phím tắt này tuỳ hệ điều hành sẽ khác nhau) để thực thi chương trình.

     <img src="https://i.imgur.com/mwtVMz9.png">

- Kết quả thực thi sẽ hiển thị ngay bên dưới cửa sổ lệnh:

     <img src="https://i.imgur.com/SEGdlPB.png">
    
- Trong PyCharm có 2 chế độ **`Run`**, các bạn có thể thực thi bằng cửa sổ **`4: Run`** thông thường hoặc dùng cửa sổ **`Python Console`**. Mình khuyến khích các bạn nên chuyển qua **`Run`** bằng cửa sổ **`Python Console`** vì chúng ta không cần in giá trị biến ra ngoài màn hình.
    - Cách chuyển qua dùng cửa sổ **`Python Console`**:
    - Trên góc bên trái phải của cửa sổ Code, các bạn vào ô như trên hình và chọn **`Edit Configuration...`**
    
      <img src="https://i.imgur.com/PxLVaYe.png">
    
    - Cửa sổ điều chỉnh hiện lên, các bạn chọn **`Run with Python Console`** trong **`Execution`** và **`Apply`** thay đổi như trong ảnh:
    
      <img src="https://i.imgur.com/JzIUyzl.png"> 
    
    - Khi này, các bạn chạy lại chương trình, file sẽ được thực thi trên cửa sổ **`Python Console`**, sẽ có thêm một cửa sổ hiện thị danh sách biến và giá trị biến lưu trữ, sẽ rất tiện dụng không cần phải hiển thị giá trị ra ngoài màn hình:

      <img src="https://i.imgur.com/8fYOWUo.png"> 
    
    - Các bạn có thể chọn **`View`** để xem chi tiết hơn:

      <img src="https://i.imgur.com/kPgMCUY.png"> 
    
    
<a name="Debug"></a>
### 2. Debug 
- Tương tự như thực thi File, các bạn chọn **`Run`** trên thanh công cụ và ấn **`Debug`** (hoặc phím tắt: **`Control + Option + D`** đối với MacOS - phím tắt này tuỳ hệ điều hành sẽ khác nhau).

- Trong trường hợp Code của bạn không có lỗi, cửa sổ **`5: Debug`** đưa ra kết quả như bình thường giống **`4: Run`**:

     <img src="https://i.imgur.com/A8cP9Zr.png"> 

- Trong trường hợp Code của bạn có lỗi, cửa sổ Debug sẽ hiện vị trí lỗi của bạn, và đặc biệt hơn là giá trị của các biến cũng được hiển thị bên cạnh, bạn có thể dễ dàng chỉnh lại lỗi của mình.
   - Trong ảnh dưới đây mình lỗi thiếu **` : `** trong  **`sorted_population[m - elitism]`**:

       <img src="https://i.imgur.com/UDaoSZy.png"> 

<a name="Tongket"></a>
## Tổng Kết  
- Tổng hợp phím tắt trong PyCharm: https://www.jetbrains.com/help/pycharm/keyboard-shortcuts-by-category.html

Bài viết trên là những kiến thức mình thu được khi học tập, hi vọng nó sẽ giúp các bạn một phần nào đó.

Cám ơn các bạn đã theo dõi! (^_^)
