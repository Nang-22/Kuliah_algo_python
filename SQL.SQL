
CREATE TABLE ktp (
    nik int,
    nama varchar(150),
    ttl varchar(50),
    alamat varchar(130),
    setatus varchar(110),
    golongan_darah varchar(110)
);

INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (123456789, 'Rizky', 'Bandung, 20-10-2000', 'Jl. Merdeka No. 123', 'Belum Menikah', 'O');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (987654321, 'Siti', 'Jakarta, 15-05-1995', 'Jl. Sudirman No. 456', 'Menikah', 'A');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (456789123, 'Andi', 'Surabaya, 10-12-1988', 'Jl. Diponegoro No. 789', 'Menikah', 'B');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (789123456, 'Dewi', 'Medan, 05-03-1992', 'Jl. Gatot Subroto No. 321', 'Belum Menikah', 'AB');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (321654987, 'Budi', 'Yogyakarta, 25-07-1985', 'Jl. Maliboro No. 654', 'Menikah', 'O');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (654987321, 'Sari', 'Semarang, 30-09-1990', 'Jl. Pandanaran No. 987', 'Belum Menikah', 'A');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (789654123, 'Agus', 'Bandung, 12-11-1987', 'Jl. Asia Afrika No. 123', 'Menikah', 'B');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (123789456, 'Rina', 'Jakarta, 18-02-1993', 'Jl. Thamrin No. 456', 'Belum Menikah', 'AB');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (456123789, 'Eko', 'Surabaya, 22-08-1989', 'Jl. Pahlawan No. 789', 'Menikah', 'O');
INSERT INTO KTP (NIK, NAMA, TTL, ALAMAT, SETATUS, GOLONGAN_DARAH) VALUES (321987654, 'Maya', 'Medan, 10-01-1991', 'Jl. Sisingamangaraja No. 321', 'Belum Menikah', 'A');

SELECT * FROM KTP
GO