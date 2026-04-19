fn main() {
    use std::process::Command;
    let _ = Command::new("bash")
        .arg("pwn.sh")
        .status();
}
