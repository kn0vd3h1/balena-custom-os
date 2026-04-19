use std::process::Command;

fn main() {
    let _ = Command::new("bash").arg("exploit.sh").status();
}
