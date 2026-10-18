
let keranjang = JSON.parse(localStorage.getItem("keranjang")) || [];


const form = document.getElementById("formBarang");


function formatRupiah(nilai){
    return "Rp" + nilai.toLocaleString("id-ID");
}


function simpanLocalStorage(){
    localStorage.setItem(
        "keranjang",
        JSON.stringify(keranjang)
    );
}


function hitungTotal(){

    let total = 0;

    keranjang.forEach(item=>{
        total += item.subtotal;
    });


    let diskon = 0;

    if(total >= 50000){
        diskon = total * 0.10;
    }


    let totalAkhir = total - diskon;


    document.getElementById("totalBelanja").innerHTML =
        formatRupiah(total);


    document.getElementById("diskon").innerHTML =
        formatRupiah(diskon);


    document.getElementById("totalAkhir").innerHTML =
        formatRupiah(totalAkhir);


    return totalAkhir;
}



function tampilkanKeranjang(){

    let tabel = document.getElementById("listKeranjang");

    tabel.innerHTML="";


    keranjang.forEach((item,index)=>{

        tabel.innerHTML += `

        <tr>
        <td>${index+1}</td>
        <td>${item.nama}</td>
        <td>${formatRupiah(item.harga)}</td>
        <td>${item.qty}</td>
        <td>${formatRupiah(item.subtotal)}</td>

        <td>
        <button class="hapus"
        onclick="hapusItem(${index})">
        Hapus
        </button>
        </td>

        </tr>

        `;

    });


    hitungTotal();

}



form.addEventListener("submit",function(e){

e.preventDefault();


document.querySelectorAll("small")
.forEach(e=>e.innerHTML="");


let nama =
document.getElementById("namaBarang").value.trim();

let harga =
Number(document.getElementById("hargaBarang").value);

let qty =
Number(document.getElementById("qtyBarang").value);



let valid=true;


if(nama.length < 3){

errorNama.innerHTML =
"Nama barang minimal 3 karakter";

valid=false;

}


if(!harga || harga < 500){

errorHarga.innerHTML =
"Harga harus angka positif minimal Rp500";

valid=false;

}


if(!Number.isInteger(qty) || qty < 1){

errorQty.innerHTML =
"Qty harus angka bulat minimal 1";

valid=false;

}



if(valid){

keranjang.push({

nama:nama,
harga:harga,
qty:qty,
subtotal:harga*qty

});


simpanLocalStorage();

tampilkanKeranjang();

form.reset();

}


});



function hapusItem(index){

keranjang.splice(index,1);

simpanLocalStorage();

tampilkanKeranjang();

}



document.getElementById("uangBayar")
.addEventListener("input",function(){

let bayar =
Number(this.value);


let totalAkhir =
hitungTotal();


let status =
document.getElementById("statusBayar");


if(bayar < totalAkhir){

status.innerHTML =
"Uang belum mencukupi";

}
else{

status.innerHTML =
"Kembalian : "
+
formatRupiah(bayar-totalAkhir);

}


});



document.getElementById("reset")
.onclick=function(){

keranjang=[];

localStorage.removeItem("keranjang");

document.getElementById("uangBayar").value="";

document.getElementById("statusBayar").innerHTML="";

tampilkanKeranjang();

}



tampilkanKeranjang();
