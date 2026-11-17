
import threading
import time
import random

import pandas as pd
import plotly.express as px
import streamlit as st

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="ThreadSync | OS Lab",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ================= CUSTOM UI ===================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 0%, #e8eaff, transparent 30%),
        #f6f8fc;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(120deg, #111827, #3730a3, #0369a1);
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px #1e293b20;
}

.hero small {
    color: #bfdbfe;
    letter-spacing: 3px;
    font-weight: 700;
}

.hero h1 {
    color: white;
    font-size: 2.5rem;
    margin: 12px 0;
}

.hero p {
    color: #dbeafe;
    font-size: 1rem;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e2e8f0;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 4px 14px #0f172a08;
}

div[data-testid="stMetricLabel"] {
    color: #64748b;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #111827;
    font-weight: 800;
}

.stButton > button {
    border-radius: 10px;
    min-height: 45px;
    font-weight: 700;
    background: linear-gradient(90deg, #4f46e5, #2563eb);
    color: white;
    border: none;
}

.stButton > button:hover {
    color: white;
    border: none;
    filter: brightness(1.1);
}

[data-testid="stSidebar"] {
    background: #111827;
}

[data-testid="stSidebar"] * {
    color: #f8fafc;
}

[data-testid="stSidebar"] [data-baseweb="select"] * {
    color: #111827;
}

.panel {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 12px;
}

.panel h3 {
    color: #111827;
}

.section-title {
    font-size: 1.5rem;
    font-weight: 800;
    color: #111827;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #64748b;
    margin-bottom: 22px;
}

.pill {
    background: #e0e7ff;
    color: #3730a3;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
}

hr {
    border-color: #e2e8f0;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER ======================

st.markdown("""
<div class="hero">
    <small>OPERATING SYSTEMS • INTERACTIVE LAB</small>
    <h1>🔄 Thread Synchronization Playground</h1>
    <p>
        Explore race conditions, mutex locks, semaphores
        and producer-consumer synchronization.
    </p>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR =====================

with st.sidebar:
    st.markdown("## 🔄 ThreadSync")
    st.caption("Operating Systems Mini Project")
    st.divider()

    module = st.radio(
        "SELECT MODULE",
        [
            "Overview",
            "Race Condition vs Mutex",
            "Semaphore Playground",
            "Producer-Consumer",
        ],
    )

    st.divider()
    st.markdown("### 📚 Concepts")
    st.markdown("- 🧵 Multithreading")
    st.markdown("- 🔐 Mutex Lock")
    st.markdown("- 🚦 Semaphore")
    st.markdown("- 📦 Shared Buffer")
    st.divider()
    st.caption("Built with Python and Streamlit")


# ================= HELPERS ======================

def section(title, subtitle):
    st.markdown(
        f'<div class="section-title">{title}</div>'
        f'<div class="section-subtitle">{subtitle}</div>',
        unsafe_allow_html=True,
    )


def show_log(log):
    if log:
        with st.expander("📋 View Execution Event Log"):
            st.dataframe(
                pd.DataFrame(log),
                use_container_width=True,
                hide_index=True,
            )


# ================= OVERVIEW ====================

if module == "Overview":

    section(
        "Welcome to the Lab",
        "Choose a module and run your first synchronization experiment.",
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="panel">
            <span class="pill">MODULE 01</span>
            <h3>⚡ Race Condition</h3>
            <p>Compare unsafe counter updates with mutex-protected updates.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="panel">
            <span class="pill">MODULE 02</span>
            <h3>🔐 Semaphore</h3>
            <p>Control how many threads can use a limited resource.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="panel">
            <span class="pill">MODULE 03</span>
            <h3>📦 Producer-Consumer</h3>
            <p>Visualize items entering and leaving a shared buffer.</p>
        </div>
        """, unsafe_allow_html=True)

    section(
        "Core OS Concepts",
        "The synchronization mechanisms demonstrated in this project.",
    )

    a, b, c = st.columns(3)
    a.metric("Threads", "Concurrent tasks")
    b.metric("Mutex", "One-at-a-time access")
    c.metric("Semaphore", "Limited resource slots")

    st.info(
        "Recommended demo: first run Race Condition vs Mutex, "
        "then Semaphore, and finally Producer-Consumer."
    )

    st.markdown("""
    <div class="panel">
        <h3>🎯 Project Objective</h3>
        Demonstrate how multiple threads access shared resources,
        how race conditions can occur, and how synchronization
        mechanisms help protect shared data.
    </div>
    """, unsafe_allow_html=True)


# ============ RACE CONDITION VS MUTEX ===========

elif module == "Race Condition vs Mutex":

    section(
        "Race Condition vs Mutex",
        "Compare multiple threads updating a shared counter.",
    )

    col1, col2 = st.columns(2)

    with col1:
        thread_count = st.slider(
            "Number of Threads",
            2, 8, 4,
            key="race_threads",
        )

    with col2:
        increments = st.slider(
            "Increments per Thread",
            10, 300, 100,
            step=10,
            key="race_increments",
        )

    mode = st.radio(
        "Execution Mode",
        ["Without Lock", "With Mutex Lock"],
        horizontal=True,
    )

    expected = thread_count * increments

    st.markdown(
        f"""
        <div class="panel">
            <b>Expected Counter</b>
            <h2>{expected:,}</h2>
            <p>
                {thread_count} threads × {increments}
                increments per thread
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "▶ Run Counter Simulation",
        type="primary",
        use_container_width=True,
    ):

        counter = [0]
        mutex = threading.Lock()
        log_lock = threading.Lock()
        logs = []

        def worker(thread_id):
            for step in range(increments):

                if mode == "With Mutex Lock":
                    with mutex:
                        counter[0] += 1

                else:
                    # Deliberately unsafe read-modify-write
                    old_value = counter[0]

                    time.sleep(
                        random.uniform(0, 0.0002)
                    )

                    counter[0] = old_value + 1

                if step == 0 or step == increments - 1:
                    with log_lock:
                        logs.append({
                            "Thread": f"T{thread_id}",
                            "Step": step + 1,
                            "Event": "Counter updated",
                        })

        threads = [
            threading.Thread(
                target=worker,
                args=(i + 1,),
            )
            for i in range(thread_count)
        ]

        start = time.perf_counter()

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        elapsed = time.perf_counter() - start

        actual = counter[0]
        lost = max(0, expected - actual)

        a, b, c, d = st.columns(4)

        a.metric("Expected Counter", f"{expected:,}")
        b.metric("Actual Counter", f"{actual:,}")
        c.metric("Lost Updates", f"{lost:,}")
        d.metric("Execution Time", f"{elapsed:.4f} s")

        if mode == "With Mutex Lock":
            st.success(
                "Mutex mode completed. The counter should "
                "match the expected value."
            )

        elif lost > 0:
            st.warning(
                "Race condition observed: some updates were lost."
            )

        else:
            st.info(
                "No lost updates appeared in this run. "
                "Race conditions depend on thread timing."
            )

        chart_data = pd.DataFrame({
            "Counter": ["Expected", "Actual"],
            "Value": [expected, actual],
        })

        fig = px.bar(
            chart_data,
            x="Counter",
            y="Value",
            color="Counter",
            text="Value",
            title="Expected vs Actual Counter",
            template="plotly_white",
        )

        fig.update_layout(
            showlegend=False,
            margin=dict(l=10, r=10, t=55, b=10),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

        show_log(logs)


# ============== SEMAPHORE PLAYGROUND ============

elif module == "Semaphore Playground":

    section(
        "Semaphore Playground",
        "Control the number of threads accessing a shared resource.",
    )

    a, b, c = st.columns(3)

    with a:
        thread_total = st.slider(
            "Number of Threads",
            2, 12, 6,
            key="sem_threads",
        )

    with b:
        capacity = st.slider(
            "Resource Slots",
            1, 6, 2,
            key="sem_capacity",
        )

    with c:
        work_time = st.slider(
            "Resource Usage Time (seconds)",
            0.01, 0.20, 0.05,
            step=0.01,
        )

    st.markdown(
        f"""
        <div class="panel">
            <h3>🚦 Semaphore Rule</h3>
            At most <b>{capacity} threads</b> should use the
            protected resource simultaneously.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "▶ Run Semaphore Simulation",
        type="primary",
        use_container_width=True,
    ):

        semaphore = threading.Semaphore(capacity)
        state_lock = threading.Lock()

        active = [0]
        peak = [0]
        logs = []

        origin = time.perf_counter()

        def sem_worker(thread_id):

            with state_lock:
                logs.append({
                    "Time (s)": round(
                        time.perf_counter() - origin, 4
                    ),
                    "Thread": f"T{thread_id}",
                    "Event": "Waiting",
                    "Active Users": active[0],
                })

            with semaphore:

                with state_lock:
                    active[0] += 1

                    peak[0] = max(
                        peak[0],
                        active[0],
                    )

                    logs.append({
                        "Time (s)": round(
                            time.perf_counter() - origin, 4
                        ),
                        "Thread": f"T{thread_id}",
                        "Event": "Entered Resource",
                        "Active Users": active[0],
                    })

                time.sleep(work_time)

                with state_lock:
                    active[0] -= 1

                    logs.append({
                        "Time (s)": round(
                            time.perf_counter() - origin, 4
                        ),
                        "Thread": f"T{thread_id}",
                        "Event": "Released Resource",
                        "Active Users": active[0],
                    })

        threads = [
            threading.Thread(
                target=sem_worker,
                args=(i + 1,),
            )
            for i in range(thread_total)
        ]

        start = time.perf_counter()

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        elapsed = time.perf_counter() - start

        x, y, z = st.columns(3)

        x.metric("Threads Completed", thread_total)
        y.metric("Resource Capacity", capacity)
        z.metric("Peak Simultaneous Users", peak[0])

        st.metric(
            "Total Execution Time",
            f"{elapsed:.3f} seconds",
        )

        if peak[0] <= capacity:
            st.success(
                "Semaphore successfully respected the resource limit."
            )
        else:
            st.error(
                "Unexpected resource capacity violation."
            )

        df = pd.DataFrame(logs).sort_values("Time (s)")

        fig = px.scatter(
            df,
            x="Time (s)",
            y="Active Users",
            color="Event",
            hover_data=["Thread"],
            title="Resource Usage Over Time",
            template="plotly_white",
        )

        fig.update_yaxes(
            dtick=1,
            rangemode="tozero",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

        show_log(logs)


# ================ PRODUCER-CONSUMER ==============

else:

    section(
        "Producer-Consumer Problem",
        "Coordinate a producer and consumer using a bounded buffer.",
    )

    a, b, c = st.columns(3)

    with a:
        buffer_capacity = st.slider(
            "Buffer Capacity",
            2, 10, 5,
            key="pc_capacity",
        )

    with b:
        item_count = st.slider(
            "Items to Produce",
            5, 30, 12,
            key="pc_items",
        )

    with c:
        delay = st.slider(
            "Operation Delay (seconds)",
            0.0, 0.10, 0.01,
            step=0.01,
            key="pc_delay",
        )

    st.markdown("""
    <div class="panel">
        <h3>📦 Synchronization Rules</h3>
        • Producer waits when the buffer is full.<br>
        • Consumer waits when the buffer is empty.<br>
        • Mutex protects the shared buffer.
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "▶ Run Producer-Consumer",
        type="primary",
        use_container_width=True,
    ):

        buffer = []

        mutex = threading.Lock()

        empty = threading.Semaphore(
            buffer_capacity
        )

        full = threading.Semaphore(0)

        logs = []
        produced = []
        consumed = []

        def producer():

            for item in range(1, item_count + 1):

                empty.acquire()

                with mutex:
                    buffer.append(item)
                    produced.append(item)

                    logs.append({
                        "Thread": "Producer",
                        "Event": f"Produced Item {item}",
                        "Buffer": str(buffer.copy()),
                        "Buffer Size": len(buffer),
                    })

                full.release()

                if delay:
                    time.sleep(delay)

        def consumer():

            for _ in range(item_count):

                full.acquire()

                with mutex:
                    item = buffer.pop(0)
                    consumed.append(item)

                    logs.append({
                        "Thread": "Consumer",
                        "Event": f"Consumed Item {item}",
                        "Buffer": str(buffer.copy()),
                        "Buffer Size": len(buffer),
                    })

                empty.release()

                if delay:
                    time.sleep(delay)

        p = threading.Thread(target=producer)
        c = threading.Thread(target=consumer)

        start = time.perf_counter()

        p.start()
        c.start()

        p.join()
        c.join()

        elapsed = time.perf_counter() - start

        x, y, z = st.columns(3)

        x.metric("Items Produced", len(produced))
        y.metric("Items Consumed", len(consumed))
        z.metric("Items Remaining", len(buffer))

        st.metric(
            "Execution Time",
            f"{elapsed:.3f} seconds",
        )

        if produced == consumed and not buffer:
            st.success(
                "Success! Every produced item was consumed. "
                "The buffer is empty."
            )
        else:
            st.error(
                "Unexpected final buffer state."
            )

        df = pd.DataFrame(logs)

        fig = px.line(
            df.reset_index(),
            x="index",
            y="Buffer Size",
            color="Thread",
            markers=True,
            title="Buffer Size After Each Event",
            template="plotly_white",
        )

        fig.update_yaxes(
            dtick=1,
            rangemode="tozero",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

        show_log(logs)


# ================= FOOTER =======================

st.divider()

st.caption(
    "ThreadSync | Operating Systems Mini Project | "
    "Python • Threading • Mutex • Semaphore • Streamlit • Plotly"
)
