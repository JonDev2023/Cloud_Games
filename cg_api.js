function LoadData(datafile_name) {
    const res = await fetch("/" + datafile_name);
    const data = await res.json();
    return data;
}