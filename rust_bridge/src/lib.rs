use pyo3::prelude::*;

#[pyfunction]
fn fast_inspect(path: String) -> PyResult<String> {
    Ok(format!("Rust engine inspected: {}", path))
}

#[pymodule]
fn claude_code_runtime(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fast_inspect, m)?)?;
    Ok(())
}
